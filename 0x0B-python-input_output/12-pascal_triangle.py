""" 
    Technical interview preparation:
    Create a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    list = []

    if (n <= 0):
        return list
    
    a = 1
    b = 1
    c = 1
    for i in range(n):
        lst = []
