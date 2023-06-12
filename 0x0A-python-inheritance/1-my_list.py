#!/usr/bin/python3
""" a class MyList that inherits from list: """


class MyList(list):
    """ This class take in a list as arguments """
    pass

    def print_sorted(self):
        """ a method that prints the list, but sorted (ascending sort) """
        new_list = sorted(self)
        print(new_list)
