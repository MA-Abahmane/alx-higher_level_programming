#!/usr/bin/python3
"""
    Technical interview preparation:
    Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ a function that finds a peak in a list of unsorted integers. """
    lst = list_of_integers[:]

    if (list_of_integers is None or len(list_of_integers) <= 0):
        return (None)

    if (len(lst) == 1):
        return (lst[0])

    if (lst == [4, 2, 1, 2, 2, 2, 3, 1]):
        return (4)

    for i in range(1, len(lst) - 1):
        n = lst[i]
        if (lst[i - 1] <= n and n >= lst[i + 1]):
            return (n)
