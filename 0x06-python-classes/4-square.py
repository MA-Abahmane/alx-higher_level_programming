#!/usr/bin/python3
""" The class Square """


class Square:
    """ The constructor """

    def __init__(self, size=0):
        self.size = size


    """ Get size """

    @property
    def size(self):
        return self.__size


    """ Get size """

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise ValueError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


 """ Area calculator """

    def area(self):
        return self.__size ** 2
