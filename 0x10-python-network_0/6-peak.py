#!/usr/bin/python3
""" 
    Technical interview preparation:
    Write a function that finds a peak in a list of unsorted integers. 
"""


def find_peak(list_of_integers):
    """ a function that finds a peak in a list of unsorted integers. """

    if (list_of_integers is None or len(list_of_integers) < 0):
        return (None)
    
    
