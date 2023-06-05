#!/usr/bin/python3
""" The N queens puzzle """


if __name__ == '__main__':
    """ inside main """

    from sys import argv


    if (len(argv) != 2):
        print('Usage: nqueens N')
        exit(1)

    if (type(argv[1]) not in [int]):
        print('N must be a number')
        exit(1)

    n = int(argv[1])

    if (n < 4):
        print('N must be at least 4')
        exit(1)



