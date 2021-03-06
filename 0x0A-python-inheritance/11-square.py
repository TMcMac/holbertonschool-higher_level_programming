#!/usr/bin/python3
"""Docstring because reasons"""


class BaseGeometry:
    """
    A mostly empty class with a few error conditions
    """
    def area(self):
        """
        Just an error for this one
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Just meant to raise errors for now
        parameters - name: a string much like key in dict
                     value: (int) much like value in a dict
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Inheriets from the class BaseGeometry which is mostly full or errors
    """
    def __init__(self, width, height):
        """
        initializes with a validity check for ints
        parameters - width (int): the width
                     height (int): the height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        calcualtes the area of our rectangle
        """
        return (self.__height * self.__width)

    def __str__(self):
        """
        returns a string representation of the object
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """
    Inheriets from class rectangle
    """
    def __init__(self, size):
        """
        Initializes a square of size size after
        validating size to be an int
        parameter - size (int): the size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        returns a string representation of the object
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
