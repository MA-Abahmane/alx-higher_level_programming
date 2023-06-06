#!/usr/bin/python3
class LockedClass:
    names_allowed = ['first_name']
    def __setattr__(self, name , value):
        if name not in self.names_allowed:
            print('[AttributeError] \'LockedClass\' object has no attribute \'last_name\'')
