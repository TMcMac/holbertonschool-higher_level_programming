#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    count = 1
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end='')
            if count < len(row):
                print(" ", end='')
            count += 1
        print()
        count = 1
