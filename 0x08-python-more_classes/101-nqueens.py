#!/usr/bin/python3
""" 
The N queens puzzle:

is the challenge of placing N non-attacking queens on an N×N 
chessboard. Write a program that solves the N queens problem.
"""

import sys


if __name__ == "__main__":
    """ 
    Entry point of the program.
    """

    if (len(sys.argv) != 2):
        print('Usage: nqueens N')
        sys.exit(1)

    if (type(sys.argv[1]) not in [int]):
        print('N must be a number')
        sys.exit(1)

    n = int(sys.argv[1])

    if (n < 4):
        print('N must be at least 4')
        sys.exit(1)



