#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard. Write 
a program that solves the N queens problem. """


from sys import argv


if (len(argv) != 2):
    print('Usage: nqueens N')
    exit(1)

n = int(argv[1])

if (type(n) not in [int]):
    print('N must be a number')
    exit(1)

if (n < 4):
    print('N must be at least 4')
    exit(1)



