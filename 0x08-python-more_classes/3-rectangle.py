#!/usr/bin/python3
"""Defining a class rectangle"""


class Rectangle():
    """
    Rectangle - a class for a polygon object
    """
    def __init__(self, width=0, height=0):
        """
        A function of class rectangle that defines
        a rectangle and calculates things like area
        and perimeter
        Args: param1: width (int) - the width
              param2: height (int) - the height
        Returns an object of class Rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width of the obj"""
        return self.__width
    @property
    def height(self):
        """Returns the height of the obj"""
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle
        Args: param: width (int) - the width
        Return: None
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = int(value)

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle
        Args: param: height (int) - the height
        Return: None
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = int(value)

    def area(self):
        """Returns the calculated area of the obj"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * self.__height)

    def perimeter(self):
        """Returns the calculated perimeter of the obj in not 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Prints out the string rep of the obj using #s"""
        obj_str = ""
        if self.__height == 0 or self.__width == 0:
            return obj_str
        else:
            for row in range(self.__height):
                for col in range(self.__width):
                    obj_str += '#'
                obj_str += '\n'
            obj_str = obj_str[:-1]
            return obj_str
