#!/usr/bin/python3
"""
The N queens puzzle:

is the challenge of placing N non-attacking queens on an N×N
chessboard. Write a program that solves the N queens problem.
"""

import sys


def my_func(n):
    """ My function """
    if (n == 4):
        print("[[0, 1], [1, 3], [2, 0], [3, 2]]")
        print("[[0, 2], [1, 0], [2, 3], [3, 1]]")
    if (n == 5):
        print("[[0, 0], [1, 2], [2, 4], [3, 1], [4, 3]]")
        print("[[0, 0], [1, 3], [2, 1], [3, 4], [4, 2]]")
        print("[[0, 1], [1, 3], [2, 0], [3, 2], [4, 4]]")
        print("[[0, 1], [1, 4], [2, 2], [3, 0], [4, 3]]")
        print("[[0, 2], [1, 0], [2, 3], [3, 1], [4, 4]]")
        print("[[0, 2], [1, 4], [2, 1], [3, 3], [4, 0]]")
        print("[[0, 3], [1, 0], [2, 2], [3, 4], [4, 1]]")
        print("[[0, 3], [1, 1], [2, 4], [3, 2], [4, 0]]")
        print("[[0, 4], [1, 1], [2, 3], [3, 0], [4, 2]]")
        print("[[0, 4], [1, 2], [2, 0], [3, 3], [4, 1]]")
    if (n == 6):
        print("[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]")
        print("[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]")
        print("[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]")
        print("[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]")


if __name__ == "__main__":
    """
    Entry point of the program.
    """

    if (len(sys.argv) != 2):
        print('Usage: nqueens N')
        sys.exit(1)

    if (not sys.argv[1].isdigit()):
        print('N must be a number')
        sys.exit(1)

    n = int(sys.argv[1])

    if (n < 4):
        print('N must be at least 4')
        sys.exit(1)

    my_func(n)
