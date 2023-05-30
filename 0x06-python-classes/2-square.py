#!/usr/bin/python3

class Square:
    """ class Square ckeck if size in a digit and is >= to 0 """
    def __init__(self, size=0):
        """ The constructor """
        if (type(size) != int):
            raise ValueError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
