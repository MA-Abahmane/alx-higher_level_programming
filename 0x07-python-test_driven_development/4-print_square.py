#!/usr/bin/python3
""" This module has a function that prints a square out of '#' """


def print_square(size):
    """ The function that prints a square of '#' with 
    a given size

    Args:
        size (int): given is the size length of the square
    """

    if (type(size) not in [int]):
        raise TypeError('size must be an integer')
    if (size < 0):
        raise ValueError('size must be >= 0')
    if (type(size) not in [int] and size < 0):
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()