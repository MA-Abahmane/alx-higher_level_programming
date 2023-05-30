#!/usr/bin/python3

class Square:
    """ class Square ckeck if size in a digit and is >= to 0 """
    def __init__(self, size=0):
        """ The constructor """
        self.size = size
    
    @property
    def size(self):
        """ Get size """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ Get size """
        if (type(value) != int):
            raise ValueError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
        
    def area(self):
        """ Area calculator """
        return self.__size ** 2
