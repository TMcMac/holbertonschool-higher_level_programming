#!/usr/bin/python3
"""Docstring"""


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
        else:
            return True


class Rectangle(BaseGeometry):
    """
    Inheriets from the class BaseGeometry which is mostly full or errors
    """
    def __init__(self, width, height):
        """
        initializes with a validity check for ints
        """
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
