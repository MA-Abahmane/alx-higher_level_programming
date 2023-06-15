#!/usr/bin/python3
""" the class Rectangle that inherits from Base: """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __str__(self):
        """ class printer """
        wth = self.width
        hit = self.height
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {wth}/{hit}")

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Rectangle width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError('width must be an integer')
        if (value <= 0):
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """ Rectangle height """
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError('height must be an integer')
        if (value <= 0):
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """ Rectangles x cordinate"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) is not int):
            raise TypeError('x must be an integer')
        if (value < 0):
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """ Rectangles x cordinate"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if (type(value) is not int):
            raise TypeError('y must be an integer')
        if (value < 0):
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """ return the area value of the Rectangle instance. """
        return (self.__height * self.__width)
    
    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        wth = self.__width
        hit = self.__height

        for line in range(self.__y):
            print()

        for i in range(hit):
            for space in range(self.__x):
                print(' ', end='')
            for j in range(wth):
                print('#', end='')
            print()
    
    def updater(self, id=None, width=None, height=None, x=None, y=None):
        """ update the values of atributes (update method helper) """
        if (width is not None):
            self.width = width
        if (height is not None):
            self.height = height
        if (x is not None):
            self.x = x
        if (y is not None):
            self.y = y
        if (id is not None):
            self.id = id

    def update(self, *args, **kwargs):
        """ 
        assigns an argument to each attribute
        **This method can update variable is 2 ways:
            - args mode (given args)
            - kwargs mode (given kwargs)
        """
        if (args):
            self.updater(*args)
        elif (kwargs):
            self.updater(**kwargs)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle  """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
