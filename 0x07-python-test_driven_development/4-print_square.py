#!/usr/bin/python3
""" A function to print a square """


def print_square(size):
    """
    print_square - will print a square using #'s
    Argument 1 - a non-zero int or float to determin size
    return - none, just print to stdout
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, int) and size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    for row in range(int(size)):
        for col in range(int(size)):
            print('#', end="")
        print()
