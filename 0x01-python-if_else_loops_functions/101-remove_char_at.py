#!/usr/bin/python3

def remove_char_at(str, n):
    str_arr = ""
    x = 0

    while (x < len(str)):
        if (x == n):
            x += 1
            continue
        else:
            str_arr += str[x]

        x += 1
    return str_arr
