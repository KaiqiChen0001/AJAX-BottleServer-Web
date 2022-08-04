import csv

def unique_values(k, lst):
    ret_val = []
    for dict in lst:
        if dict[k] not in ret_val:
            ret_val.append(dict[k])
    return ret_val


def filter_list(k, v, lst):
    ret_val = []
    for dict in lst:
        if dict[k] == v:
            ret_val.append(dict)
    return ret_val


def dict_gen(keys, values):
    ret_val = {}
    length = len(keys)
    for x in range(length):
        ret_val[keys[x]] = values[x]
    return ret_val


def get_values(keys, dic):
    ret_val = []
    for key in keys:
        ret_val.append(dic[key])
    return ret_val



def header_writer(lst, f_out):
    with open(f_out, 'w') as f:
        file = csv.writer(f)
        file.writerow(lst)


def data_writer(lst, f_out):
    with open(f_out, 'a') as f:
        file = csv.writer(f)
        for list in lst:
            file.writerow(list)









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


def forlinechart():
  listofdate = []
  with open('cache.csv') as f:
    file = csv.reader(f)
    next(file)
    for row in file:
      if not row == []:
        listofdate.append(row[0])
  listofdate.sort()
  dic_count = {}
  for date in listofdate:
    dic_count[date] = dic_count.get(date, 0) + 1
  xlist = []
  ylist = []
  for x in dic_count.keys():
    xlist.append(x)
  for y in dic_count.values():
    ylist.append(y)
  trace = {'x':xlist, 'y':ylist, 'type': 'scatter' }
  return [trace]

def forpiechart():
  with open('cache.csv') as f:
    file = csv.reader(f)
    next(file)
    dict = {}
    for row in file:
      boro = row[3]
      dict[boro] = dict.get(boro, 0) + 1
    numberlist = []
    borolist = []
    for boro in dict.keys():
      borolist.append(boro)
    for number in dict.values():
      numberlist.append(number)
    data = [{'values':numberlist, 'labels': borolist, 'type':'pie'} ]
    layout = {'height':400, 'width':500}
    return [data, layout]