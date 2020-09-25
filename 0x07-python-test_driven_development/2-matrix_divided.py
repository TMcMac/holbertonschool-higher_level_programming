#!/usr/bin/python3
""" A Function to divide all numbers in a matrix """


def matrix_divided(matrix, div):
    """
    matrix_divided - a function that will divide all numbers in
    a matrix by a provided divisor
    arg1: must be a list of lists of ints or floats and all lists
    must be of the same size
    arg2: must be a non zero int or float
    return: a new matrix containing all the products of the division
    rounded to two places.
    """
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    rows = len(matrix)
    columns = len(matrix[0])
    if columns == 0 and rows != 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    elif rows == 0 and columns != 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    elif rows and columns is None:
        return None
    for alist in matrix:
        if not isinstance(alist, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        elif len(alist) != columns:
            raise TypeError('Each row of the matrix must have the same size')
        temp_list = []
        for num in alist:
            if not isinstance(num, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            temp_list.append(round((num / div), 2))
        new_matrix.append(temp_list)
    return new_matrix
