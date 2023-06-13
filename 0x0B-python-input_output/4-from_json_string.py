#!/usr/bin/python3
"""
    a function that returns an object (Python data structure)
    represented by a JSON string:
"""


def from_json_string(my_str):
    """ Return JSON object representation of my_str """
    import json

    """
        json. loads() returns a Python dictionary object from
        a JSON formatted string
    """
    return (json.loads(my_str))
