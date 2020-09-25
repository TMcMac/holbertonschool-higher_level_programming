#!/usr/bin/python3
"""A simple function to add two numbers"""


def add_integer(a, b=98):
    """
    add_integer - a function to add two numbers
    parameters can only be ints or floats
    arg1: an int or a float
    arg2: an int of a float, default 98
    return: the sum of int(arg1) + int(arg2)
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
