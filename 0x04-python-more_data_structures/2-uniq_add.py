#!/usr/bin/python3

def uniq_add(my_list=[]):
    # convert the list into a set
    st = set(my_list)

    # sum values
    sum = 0
    for i in st:
        sum += i
    return (sum)
