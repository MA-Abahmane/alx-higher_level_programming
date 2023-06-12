#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py """


class BaseGeometry:
    """ Inside empty class BaseGeometry """

    def area(self):
        """ Error raising method """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ value validating method 
        Args: 
            name (string): value name
            value (int): given digit value
        Raises:
            if value not a digit return TypeError
            if value less/equal to 0 return ValueError
            """

        if (type(value) != int):
            raise TypeError('{} must be an integer'.format(name))
        if (value <= 0):
            raise ValueError('{} must be greater than 0'.format(name))
