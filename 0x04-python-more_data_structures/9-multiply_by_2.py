#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    dict_cpy = a_dictionary.copy()
    #get each key/value from dict, then multiply its value
    for key, val in dict_cpy.items():
        dict_cpy[key] = val*2

    return (dict_cpy)
