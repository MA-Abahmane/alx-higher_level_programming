#!/usr/bin/python3
""" a method that returns the list of attributes and methods of an object: """


def lookup(obj):
    """
    Args:
        obj: given class object
    Returns:
        list of available attributes and methods of an object
    """
    return (dir(obj))
