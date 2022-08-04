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
