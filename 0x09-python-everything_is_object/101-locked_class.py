#!/usr/bin/python3
""" 
Write a function magic_string() that returns a string 
“BestSchool” n times the number of the iteration (see code): 
"""


class LockedClass:
    """ class contains a function returning a string """

    names_allowed = ['first_name']

    def __setattr__(self, name , value):
        """ returns a string “BestSchool” n times the number of the iteration """

        if name not in self.names_allowed:
            print('[AttributeError] \'LockedClass\' object has no attribute \'last_name\'')
