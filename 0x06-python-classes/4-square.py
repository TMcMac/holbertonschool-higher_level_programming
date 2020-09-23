#!/usr/bin/python3
"""Defines class square and takes in a size to intialize square"""


class Square():
    """A basic class of a square that will take in size
    which must be an int and will be used for both height
    and for the width of the square as they are equal"""
    def __init__(self, size=0):
        """When you initialize a square do so with provided
        or set the defualt to 0."""
        self.size = size

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Just returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """When you set size of a square, check that size is an
        int and if so set its size else raise an error"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
