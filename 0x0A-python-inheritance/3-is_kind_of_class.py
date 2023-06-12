#!/usr/bin/python3
""" a method that check if the object is somewhat an instance of the class """


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object the test
        a_class: given class
    Returns:
        True if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class.
        otherwise False.
    """
    a = isinstance(obj, a_class)
    return(a)
