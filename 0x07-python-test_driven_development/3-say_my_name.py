#!/usr/bin/python3
""" This module has a function that devides all matrix elememts """


def say_my_name(first_name, last_name=""):
    """ The function is given a first/last name to print

    Args:
        first_name (str): given first name
        last_name (str): given last name

    Returns:
        My name is (first/last name) """

    if (isinstance(first_name, str) is False):
        raise TypeError('first_name must be a string')

    if (isinstance(last_name, str) is False):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
