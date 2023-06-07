#!/usr/bin/python3
"""
This mudul contains a function that
multiplies 2 matrices by using the module NumPy
"""
import numpy as npy


def lazy_matrix_mul(m_a, m_b):
    """ Yup, this is the one """

    result = npy.matmul(m_a, m_b)
    return (result)
