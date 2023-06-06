#!/usr/bin/python3
"""
Write a function magic_string() that returns a string
“BestSchool” n times the number of the iteration (see code):
"""


class LockedClass:
    """ class contains a function returning a string """
    names_allowed = ['first_name']
    __slots__ = names_allowed


"""
[!] By specifying __slots__, you limit the class to only
allow attributes with the names provided in the list
"""
