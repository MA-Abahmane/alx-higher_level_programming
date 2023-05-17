#!/usr/bin/python3

def roman_to_int(roman_string):

    if (roman_string is None or type(roman_string) != str):
        return (0)

    Rnum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_n = 0
    n = 0

    for c in roman_string:
        # If given character not a roman number
        if (Rnum.get(c, 0) == 0):
            return (0)

        Cval = Rnum[c]
        # if the previous Rnum was less then the current one
        if (prev_n < Cval):
            n -= (2 * prev_n)
        # else; add the number and save a previous number
        n += Cval
        prev_n = Cval

    return (n)
