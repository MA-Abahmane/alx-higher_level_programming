#!/usr/bin/python3
""" 
    Technical interview preparation:
    Create a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """ Creat the Pascal Triangle """
    pascalT = []

    if (n <= 0):
        return pascalT

    for row in range(n):
        crnt_rw = []

        # add 1 at the biginning
        crnt_rw.append(1)

        for i in range(1, row + 1):
            if (i is row):
                 crnt_rw.append(1)
                # add 1 at the end
            else:
                num = (pascalT[row - 1][i - 1] + pascalT[row - 1][i])
                crnt_rw.append(num)

        # add row to the pascal list
        pascalT.append(crnt_rw)
    return (pascalT)
