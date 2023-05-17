#!/usr/bin/python3

def weight_average(my_list=[]):
    if (my_list is None):
        return None

    divisor = 0
    for tpl in my_list:
        divisor += tpl[1]

    dividend = 0
    for tpl in my_list:
        mul = tpl[0] * tpl[1]
        dividend += mul

    return (dividend/divisor)
