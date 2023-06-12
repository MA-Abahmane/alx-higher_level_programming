#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


class BaseGeometry:
    """ Inside empty class BaseGeometry """

    def area(self):
        """ Error raising method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ value validating method """

        if (type(value) not in [int]):
            raise TypeError('{} must be an integer'.format(name))
        if (value < 1):
            raise ValueError('{} must be greater than 0'.format(name))
