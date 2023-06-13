#!/usr/bin/python3
"""
    a function that inserts a line of text to a file,
    after each line containing a specific string:
"""


def append_after(filename="", search_string="", new_string=""):
    """ fist, we open the file to read mode and save its lines
    Args:
        filename (str): given file name
        search_string (str): the string to search for
        new_string (str): the string a append is search string is found
    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as fl:
        lns = fl.readlines()

    new_lns = []

    """
        now we look for the given search string in each line
        if found, add the new string right after that line
    """
    for ln in lns:
        new_lns.append(ln)

        if (search_string in ln):
            new_lns.append(new_string)

    """ lastly, we add our new lines to the file after clearing it """
    with open(filename, 'w', encoding="utf-8") as fle:
        fle.writelines(new_lns)
