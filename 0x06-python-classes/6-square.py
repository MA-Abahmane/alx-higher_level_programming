#!/usr/bin/python3
"""The class Square"""


class Square:
    """inside class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialise squares.

        Args:
            size (int): ssquare size.
            position (tuple): given space indexs
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Set position as a private instance attributes """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Check if the value passes is a tuple with 2 digits """
        if (type(value) != tuple or value[0] and value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2 or type(value[0]) and type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Area calculator """
        return (self.__size ** 2)

    def my_print(self):
        """ printing function """
        value = self.size

        if (value == 0):
            print()
        else:
            x, y = self.position
            for i in range(y):
                print()
            for j in range(value):
                print(x * ' ', end="")
                print(value * '#')
