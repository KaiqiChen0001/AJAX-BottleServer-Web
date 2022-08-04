import csv

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


