#!/usr/bin/python3
""" The class Square """


class Square:
    """ inside class Square """

    def __init__(self, size=0):
        """ initialise squares

        Args:
        size (int): square suze.
        """
        self.size = size

    @property
    def size(self):
        """ set size as a private instance attributes """
        return self.__size

    @size.setter
    def size(self, value):
          """ check if size is a digit and in not a negative one """
        if (type(value) != int):
            raise ValueError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
         """ Area calculator """
        return self.__size ** 2
