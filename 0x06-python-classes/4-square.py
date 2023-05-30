#!/usr/bin/python3
"""The class Square"""


class Square:
    """inside class Square"""

    def __init__(self, size=0):
        """initialise squares.

        Args:
            size (int): square size.
        """
        self.size = size

    @property
    def size(self):
        """Set size as a private instance attributes."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Area calculator"""
        return (self.__size ** 2)
