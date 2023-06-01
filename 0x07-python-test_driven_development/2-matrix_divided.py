#!/usr/bin/python3
""" This module has a function that devides all matrix elememts """


def matrix_divided(matrix, div):
    """ The matrix function is given a 2D list and a divisor
    
    Args:
        matrix (2D list): given 2D list
        div (int): given divisor
        
    Returns:
        2D matix: The new list after division """

    err_mess = 'matrix must be a matrix \
(list of lists) of integers/floats'

    if (type(matrix) not in [list] or matrix == []):
        raise TypeError(err_mess)
    
    if (type(div) not in [int, float]):
        raise TypeError('div must be a number')
    if (div == 0):
        raise ZeroDivisionError('division by zero')

    Rsize = len(matrix[0])

    for lst in matrix:
        if (type(lst) != list or lst == []):
            raise TypeError(err_mess)

        if (len(lst) != Rsize):
            raise TypeError('Each row of the matrix must have the same size')

        for i in lst:
            if (type(i) not in [int, float]):
                raise TypeError(err_mess)


    return [[round(i / div, 2) for i in lst]for lst in matrix]