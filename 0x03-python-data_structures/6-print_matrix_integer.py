#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    mother_list = (len(matrix) - 1)
    child_list = len(matrix[0])
    for x in mother_list:
        for y in child_list:
            if (y == child_list):
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print()

