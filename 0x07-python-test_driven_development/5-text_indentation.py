#!/usr/bin/python3
""" This module has a function that prints a indents strings """


def text_indentation(text):
    """  a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): given string to indent
    """
    if (isinstance(text, str) is False):
        raise TypeError('text must be a string')
    
    char_list = ['.', '?', ':']

    chars = list(text)
    for i in range(0, len(chars)):
        if (chars[i] in char_list):
            print(chars[i], end='')
            print('\n')
        elif (chars[i - 1] in char_list and chars[i] == ' '):
            continue
        else:
            print(chars[i], end='')