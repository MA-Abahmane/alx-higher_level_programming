#!/usr/bin/python3
"""
    a function that writes a string to a text file (UTF8) and
    returns the number of characters written:
"""


def write_file(filename="", text=""):
    """ open file and write text in it
    Args:
        filename (str): given file name
        text (str): text to append to file
    Return:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as fl:
        return (fl.write(text))
