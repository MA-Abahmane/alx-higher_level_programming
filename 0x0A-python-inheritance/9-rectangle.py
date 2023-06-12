#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inside class Rectangle that inherits  from class BaseGeometry """

    def __str__(self):
        """ class printer """
        return f'[{__class__.__name__}] {self.__width}/{self.__height}'

    def __init__(self, width, height):
        """ constructor """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ new area counter """
        return (self.__width * self.__height)
