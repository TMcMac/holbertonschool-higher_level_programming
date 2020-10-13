#!/usr/bin/python3
"""For class square"""
from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """
    This is a class of rectangle with equal height and width
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an object of type square
        param1: size = height and width
        param2: horizontal offset
        param3: vertical offset
        param4: custom id, if none autogen
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        A method to return a string rep of the object
        """
        s = self.size
        x = self.x
        y = self.y
        i = self.id
        return("[Square] ({}) {}/{} - {}".format(i, x, y, s))

    def to_dictionary(self):
        """
        Returns a readable dictionary of the attributes
        """
        sqr_dict = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
        return sqr_dict

    @property
    def size(self):
        """
        Get the value of width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set the value of width
        Parameter - value, an int
        """
        self.width = value
        self.height = value
