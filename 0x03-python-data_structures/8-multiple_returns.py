#!/usr/bin/python3

def multiple_returns(sentence):

    str_len = len(sentence)

    if (str_len == 0):
        fst_char = None
    else:
        fst_char = sentence[0]

    return str_len, fst_char

