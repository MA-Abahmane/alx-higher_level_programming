#!/usr/bin/python3

def weight_average(my_list=[]):
    if (not my_list):
        return None

    divisor = 0
    for i, j in my_list:
        divisor += j

    dividend = 0
    for x, y in my_list:
        dividend += x * y

    return (dividend/divisor)
