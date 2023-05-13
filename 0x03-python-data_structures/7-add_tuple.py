#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Declarinton of empty tupls
    a = ()
    b = ()

    a_len = len(tuple_a)
    b_len = len(tuple_b)

    # Seting the needed tuples for the addition process
    if (a_len == 0):
        a = (0, 0)
    elif (a_len == 1):
        a = (tuple_a[0], 0)
    elif (a_len >= 2):
        a = (tuple_a[0], tuple_a[1])

    if (b_len == 0):
        b = (0, 0)
    elif (b_len == 1):
        b = (tuple_b[0], 0)
    elif (b_len >= 2):
        b = (tuple_b[0], tuple_b[1])

    # Addition process / return
    return (a[0] + b[0], a[1] + b[1])
