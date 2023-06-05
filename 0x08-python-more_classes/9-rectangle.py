#!/usr/bin/python3
""" class Rectangle that defines a rectangle by given indexs """


class Rectangle:
    """ inside the class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __str__(self):
        """ return string representation of an object """
        return (self.my_str())

    def __repr__(self):
        """ return string representation of an object """
        clsName = __class__.__name__
        return f'{clsName}{self.__width, self.__height}'

    def __del__(self):
        """ print a delete message """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """ Our constructor """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def my_str(self):
        """ string building method """
        strn = ""
        for i in range(self.height):
            for j in range(self.width):
                try:
                    strn += str(self.print_symbol)
                except Exception:
                    strn += type(self).print_symbol
            if (i is not self.__height - 1):
                strn += "\n"
        return (strn)

    def printer(self):
        """ string printing function """
        print()
        print(self.my_str(), end='')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if (type(rect_1) not in [Rectangle]):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if (type(rect_2) not in [Rectangle]):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if (rect_1.area() < rect_2.area()):
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """  returns a new Rectangle instance with width == height == size """
        return Rectangle(size, size)
