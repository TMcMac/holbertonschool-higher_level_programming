#!/usr/bin/python3
"""Defines class square and takes in a size to intialize square"""


class Square():
    """Class Square for building a square of #s"""
    def __init__(self, size=0):
        """Initializes an instance of square"""
        self.size = size

    def area(self):
        """Squares the size to get the area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Just a call to get the size of a side"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) != int or float:  # If its not an int or a flt
            raise TypeError("size must be a number")
        elif value < 0:  # If it is a neg number
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
