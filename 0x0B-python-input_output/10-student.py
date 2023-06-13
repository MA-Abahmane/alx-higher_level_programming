#!/usr/bin/python3
"""
    a class Student that defines a student
"""


class Student:
    """ inside class Student """

    def __init__(self, first_name, last_name, age):
        """ constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return Object dictionary description of Student """
        my_dict = {}

        """
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved
        """
        if (type(attrs) == list):
            for ky in attrs:
                if (ky in self.__dict__):
                    my_dict[ky] = self.__dict__[ky]
            return (my_dict)

        return (self.__dict__)
