#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []

    def square(n):
        return (n ** 2)
    for row in matrix:
        new_matrix.append(list(map(square, row)))
    return new_matrix
