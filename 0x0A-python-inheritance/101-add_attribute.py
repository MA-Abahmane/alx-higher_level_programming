#!/usr/bin/python3
""" a function that adds a new attribute to an object if it’s possible: 
"""


def add_attribute(obj, name, value):
    """ Lets first check if the object supports adding a new
        atribute, if not; raise TypeError
    """

    """ if object has attribute  __dict__ then it allows
        new attribute creation
    """
    if (hasattr(obj, '__dict__')):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')


"""
the __dict__ attribute is a dictionary that stores the attributes
"""

