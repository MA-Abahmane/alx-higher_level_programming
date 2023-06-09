#!/usr/bin/python3
""" class Rectangle that defines a rectangle by given indexs """


class Rectangle:
    """ inside the class Rectangle"""

    def __init__(self, width=0, height=0):
        """ Our constructor """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ return the private atributes value """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the private atributes value """
        if (type(value) not in [int]):
            raise TypeError('width must be an integer')
        if (value < 0):
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ return the private atributes value """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set the private atributes value """
        if (type(value) not in [int]):
            raise TypeError('height must be an integer')
        if (value < 0):
            raise ValueError('height must be >= 0')

        self.__height = value

    def perimeter(self):
        """ returns the rectangle perimeter """
        if (self.__height == 0 or self.__width == 0):
            return(0)
        return ((self.__height + self.__width) * 2)

    def area(self):
        """ returns the rectangle area """
        return (self.__height * self.__width)
