#!/usr/bin/python3
"""The class Square"""


class Square:
    """inside class Square"""

    def __init__(self, size=0):
        """initialise squares.

        Args:
            size (int): ssquare size.
        """
        self.size = size

    @property
    def size(self):
        """ Set size as a private instance attributes """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Check if the value passes is a positive digit """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Area calc """
        return (self.__size * 2)

    """ is equal """
    def __eq__(self, other):
        return self.area() == other.area()

    """ is not equal """
    def __ne__(self, other):
        return self.area() != other.area()

    """ is litte that """
    def __lt__(self, other):
        return self.area() < other.area()

    """ is greater that """
    def __gt__(self, other):
        return self.area() > other.area()

    """ is little or equal """
    def __le__(self, other):
        return self.area() <= other.area()

    """ is greater or equal """
    def __ge__(self, other):
        return self.area() >= other.area()
