#!/usr/bin/python3
""" Class MagicClass """
import math


class MagicClass:
    """ inside MagicClass """

    def __init__(self, radius=0):
        """ Disassembly of __init__: 
 
        Args:
            radius (int): given radius value"""

        self.__radius = 0

        if (type(radius) is not int and type(radius) is not float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ Disassembly of area: """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Disassembly of circumference: """
        return (self.__radius * math.pi * 2)
