#!/usr/bin/python3

def multiply_by_2(a_dictionary):
# get each key and value from dict then multiply its value
    return ({key: val * 2 for key, val in a_dictionary.items()})
