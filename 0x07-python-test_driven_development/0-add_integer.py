#!/usr/bin/python3
"""
Write a function that adds 2 integers.
    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, otherwise raise a TypeError exception
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    This function takes in 2 digits and returns their sum
    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: The sum of a and b
    """

    if (type(a) not in [int, float]):
        raise TypeError('a must be an integer')
    if (type(b) not in [int, float]):
        raise TypeError('b must be an integer')

    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)

    return a + b
