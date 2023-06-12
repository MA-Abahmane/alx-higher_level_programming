#!/usr/bin/python3
""" a method that check if object is exactly an instance of a the class """


def is_same_class(obj, a_class):
    """
    Args:
        obj: object the test
        a_class: given class
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False.
    """
    if (type(obj) != a_class):
        return (False)
    return(True)
