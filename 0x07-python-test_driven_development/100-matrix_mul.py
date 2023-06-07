#!/usr/bin/python3
""" this Module contains a method that multiplies 2 matrices """


def matrix_mul(m_a, m_b):
    """Function a function that multiplies 2 given matrices

    Args:
        m_a (2D list): given matrix a.
        m_b (2D list): given matrix b.

    Returns:
        A 2D list of multiplied numbers from both matrices
        if no problem incountered
    """

    if (type(m_a) not in [list]):
        raise TypeError('m_a must be a list')
    if (type(m_b) not in [list]):
        raise TypeError('m_b must be a list')

    if (m_a == [] or m_a == [[]]):
        raise ValueError('m_a can\'t be empty')
    if (m_b == [] or m_b == [[]]):
        raise ValueError('m_b can\'t be empty')

    for lst in (m_a):
        if (type(lst) not in [list]):
            raise TypeError('m_a must be a list of lists')
    for lst in (m_b):
        if (type(lst) not in [list]):
            raise TypeError('m_b must be a list of lists')

    for lst in (m_a):
        for i in lst:
            if (type(i) not in [int, float]):
                raise TypeError('m_a should contain only integers or floats')
    for lst in (m_b):
        for i in lst:
            if (type(i) not in [int, float]):
                raise TypeError('m_b should contain only integers or floats')

    size_a = len(m_a[0])
    for lst in (m_a):
        if (len(lst) != size_a):
            raise TypeError('each row of m_a must be of the same size')

    size_b = len(m_b[0])
    for lst in (m_b):
        if (len(lst) != size_b):
            raise TypeError('each row of m_b must be of the same size')

    if (len(m_a[0]) != len(m_b)):
        raise ValueError('m_a and m_b can\'t be multiplied')

    invrted_b = []
    """ Convert m_bs columns to rows:  """
    i = 0
    while (i < len(m_b[0])):
        rw = []
        lst = 0
        while (lst < len(m_b)):
            rw.append(m_b[lst][i])
            lst += 1
        invrted_b.append(rw)
        i += 1

    new_matrix = []
    """ Matrix multiplication process  """
    for rw in m_a:
        lst = []
        for cl in invrted_b:
            ansr = 0
            for idx in range(len(invrted_b[0])):
                ansr += cl[idx] * rw[idx]
            lst.append(ansr)
        new_matrix.append(lst)

    return (new_matrix)
