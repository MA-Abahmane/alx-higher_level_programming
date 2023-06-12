#!/usr/bin/python3
""" more class base """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ class print """
        return ("[Square] {}/{}".format(str(self.__size), str(self.__size)))
