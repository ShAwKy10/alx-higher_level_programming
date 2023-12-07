#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for k in a_dictionary:
        if a_dictionary[k] == value:
            keys_to_del.append(k)
    for k in keys_to_del:
        del a_dictionary[k]
    return a_dictionary
