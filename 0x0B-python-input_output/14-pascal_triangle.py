#!/usr/bin/python3

def pascal_triangle(n=0):
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    row_count = 1
    while row_count < n:
        new_row = []
        i = 0
        while i < len(triangle[row_count - 1]):
            if i == 0:
                new_row.append(1)
            else:
                new_row.append(triangle[row_count - 1][i] + triangle[row_count - 1][i - 1])
            i += 1
        new_row.append(1)
        triangle.append(new_row)
        row_count += 1
    return triangle