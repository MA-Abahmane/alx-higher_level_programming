#!/usr/bin/python3
"""
    Write a function that writes an Object to a text file,
    using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """ write my_objs JSON representation in a file """
    import json

    with open(filename, 'w', encoding="utf-8") as fl:
        json.dump(my_obj, fl)
