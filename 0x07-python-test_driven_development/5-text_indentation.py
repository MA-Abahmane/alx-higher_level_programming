#!/usr/bin/python3
""" This module has a function that prints a indents strings """


def text_indentation(text):
    """  a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): given string to indent
    """
    if (not isinstance(text, str)):
        raise TypeError('text must be a string')

    char_list = ['.', '?', ':']
    """
    split the lines of text by replacing
    eachcharacter with itseld and 2 lines
    """
    for char in char_list:
        text = text.replace(char, char + '\n\n')

    lines = []
    """
    append the stripped version (without
    leading or trailing whitespace) to the list.
    """
    for ln in text.split('\n'):
        lines.append(ln.strip())

    """ unpacks the lines list line by line """
    print(*lines, sep='\n', end='')
