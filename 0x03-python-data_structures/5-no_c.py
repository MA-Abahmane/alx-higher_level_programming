#!/usr/bin/python3

def no_c(my_string):

    i = 0
    list_len = len(my_string)
    new_list = ""
    while (i < list_len):
        if (my_string[i] == "C" or my_string[i] == 'c'):
            i += 1
            continue
        else:
            new_list += my_string[i]
        i += 1

    return new_list
