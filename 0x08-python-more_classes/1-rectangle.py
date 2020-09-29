#!/usr/bin/python3
""" This time we are making a real definition """


class Rectangle():
    """This class will define the basics of a rectangle"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val < 0:
            raise ValueError('height must be >= 0')
        self.__height = int(val)

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')
        self.__width = int(val)
