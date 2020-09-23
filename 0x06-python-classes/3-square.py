#!/usr/bin/python3
"""For this exercise we will take in the size of our square"""


class Square:
    """A basic class of a square that will take in size"""
    def __init__(self, size=0):
        """When you initialize a square, check that size is an
        int and if so set its size else raise an error"""
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
