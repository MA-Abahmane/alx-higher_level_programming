#!/usr/bin/python3
""" a function that check if the given object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: object the test
        a_class: given class
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False.
    """
    if (isinstance(obj, a_class) and type(obj) != a_class):
        return (True)
    return(False)
