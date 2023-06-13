#!/usr/bin/python3
"""
    a function that creates an Object from a “JSON file”:
"""


def load_from_json_file(filename):
    """ load/return the contents of the given json file """
    import json

    with open(filename, 'r', encoding="utf-8") as fl:
        return (json.load(fl))
