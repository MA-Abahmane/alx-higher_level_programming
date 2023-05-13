#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    list_cpy = my_list[:]
    list_len = len(my_list)

    if (idx < 0):
        return my_list
    if (idx > (list_len - 1)):
        return my_list

    list_cpy[idx] = element
    return list_cpy
