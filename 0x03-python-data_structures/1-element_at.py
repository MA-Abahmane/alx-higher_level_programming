#!/usr/bin/python3

def element_at(my_list, idx):

    list_len = len(my_list)
    if (idx < 0):
        return None
    if (idx > (list_len - 1)):
        return None
    i = 0
    while (i < list_len):
        if (i == idx):
            return my_list[i]
        i += 1

