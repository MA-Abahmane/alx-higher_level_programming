#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    lst = list()
    # save all the key to delete in a dict
    for key in a_dictionary:
        if (a_dictionary[key] == value):
            lst.append(key)
    # now delete ech key with containg value
    for key in lst:
        del a_dictionary[key]

    return (a_dictionary)
