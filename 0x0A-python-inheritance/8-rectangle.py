#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


class BaseGeometry:
    """ Inside class BaseGeometry """

    def area(self):
        """ Error raising method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ value validating method """
        if (type(value) not in [int]):
            raise TypeError('{} must be an integer'.format(name))
        if (value < 1):
            raise ValueError('{} must be greater than 0'.format(name))


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
