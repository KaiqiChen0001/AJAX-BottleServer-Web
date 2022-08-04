import csv
import json
import urllib.request

def clean_list(string, listofdict):
    retval = []
    for dict in listofdict:
        if string in dict:
            retval.append(dict)
    return retval


def dict_gen(keys, values):
    ret_val = {}
    length = len(keys)
    for x in range(length):
        ret_val[keys[x]] = values[x]
    return ret_val

def header_reader(f_in):
    with open(f_in) as f:
        file = csv.reader(f)
        header = next(file)
    return header

def data_reader(f):
    data = []
    with open(f) as file:
        realfile = csv.reader(file)
        next(realfile)
        for row in realfile:
            data.append(row)
    return data

def cache_reader(csv):
    retval = []
    header = header_reader(csv)
    data = data_reader(csv)
    for arow in data:
        retval.append(dict_gen(header, arow))
    return retval


def cache_writer(listofdict, string):
    def header_writer(lst, f_out):
        with open(f_out, 'w') as f:
            file = csv.writer(f)
            file.writerow(lst)

    def data_writer(lst, f_out):
        with open(f_out, 'a') as f:
            file = csv.writer(f)
            for list in lst:
                file.writerow(list)

    header = listofdict[0].keys()
    header_writer(header, string)
    datas = []
    for dict in listofdict:
        datas.append(dict.values())
    data_writer(datas,string)


def retrieve_json(url):
    request = urllib.request.urlopen(url)
    jsonstring = request.read().decode()
    data = json.loads(jsonstring)
    return data