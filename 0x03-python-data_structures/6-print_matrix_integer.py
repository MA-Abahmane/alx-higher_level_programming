#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    mother_list = len(matrix)
    child_list = len(matrix[0])

    i = 0
    while (i < mother_list):
        j = 0
        while (j < child_list):
            if (j == (child_list - 1)):
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
            j += 1
        print()
        i += 1
 
