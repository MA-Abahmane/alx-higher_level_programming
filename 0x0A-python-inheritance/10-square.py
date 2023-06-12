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


class Square(Rectangle):
    """ Inside class Square that inherits  from class Rectangle """

    def __init__(self, size):
        """ square constructor """
        self.__size = size

        # Running the superclass (Rectangle) constructor:
        # super() is suited for this operation
        super().__init__(self.__size, self.__size)
