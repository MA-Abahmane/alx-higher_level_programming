#!/usr/bin/python3
""" 
    Technical interview preparation:
    Write a function that finds a peak in a list of unsorted integers. 
"""


def find_peak(list_of_integers):
    """ a function that finds a peak in a list of unsorted integers. """
    lst = list_of_integers[:]

    if lst:
        lst.sort()
        return lst[-1]
    else:
        return None
