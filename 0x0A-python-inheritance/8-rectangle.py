#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inside class Rectangle that inherits  from class BaseGeometry """

    def __init__(self, width, height):
        """ constructor """
        # check is given variable are digits
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # if digits; set variables
        self.__width = width
        self.__height = height
