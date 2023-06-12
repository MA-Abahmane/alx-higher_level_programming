#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


Rectangle = __import__('9-rectangle').Rectangle


""" Class Square """


class Square(Rectangle):
    """ Inside class Square that inherits  from class Rectangle """

    def __init__(self, size):
        """ square constructor """
        self.__size = size

        # Running the superclass (Rectangle) constructor:
        # super() is suited for this operation
        super().__init__(self.__size, self.__size)
