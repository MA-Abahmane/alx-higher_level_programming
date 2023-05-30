#!/usr/bin/python
""" Class MagicClass """
import math


class MagicClass:

    def __init__(self, radius=0):
      """ Disassembly of __init__: 

      Args:
         radius (int): given radius value
      """
      self.__radius = 0

    @property
    def radius(self):
        """ return the radius """
        return self.radius

    @radius.setter
    def radius(self, val):
        """ set radius """
        if (type(val) is not int and type(val) is not float):
            raise TypeError('radius must be a number')
        else:
            self.__radius = val
    
    def area(self):
        """ Disassembly of area: """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Disassembly of circumference: """
        return (self.__radius * math.pi * 2)
