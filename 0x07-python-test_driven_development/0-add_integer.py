#!/usr/bin/python3
""" This module has the function 'add_integer' used for addition """


def add_integer(a, b=98):
    """ This function takes in 2 digits and returns their sum 

    Args:
        a (int): first number
        b (int): second number 
    Returns:
        int: The sum of a and b """

    if (type(a) not in [int, float]):
        raise TypeError('a must be an integer')
    if (type(b) not in [int, float]):
        raise TypeError('b must be an integer')

    if (type(a) is float):
        a = int(a)
    if (type(b) is float):
        b = int(b)

    return (a + b)
