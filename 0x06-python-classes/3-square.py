#!/usr/bin/python3
""" class Square now return the area of the number entered """


class Square:
    """ The constructor """

    def __init__(self, size=0):
        if (type(size) != int):
            raise ValueError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Area calculator """

    def area(self):
        return self.__size ** 2
