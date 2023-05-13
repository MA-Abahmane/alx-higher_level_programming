#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # original list pointer
    list = my_list
    list_len = len(my_list)

    if (idx < 0 or idx >= list_len):
        return my_list

    # delete element at index / return
    del list[idx]
    return list
