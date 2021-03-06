#!/usr/bin/python3
"""A definition of a class"""


class Rectangle():
    """
    A class for foursided polygons
    """
    def __init__(self, width=0, height=0):
        """
        Initialize an object of class rectangle
        Param1: the width, >=0, must be an int
        Param2: the height, >=0, must be an int
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @width.setter
    def width(self, val):
        """
        Function to set the width
        Param1: the provided width, must be int
        """
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')
        self.__width = val

    @height.setter
    def height(self, val):
        """
        Function to set height
        Param1: the prodived height, must be int
        """
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val < 0:
            raise ValueError('height must be >= 0')
        self.__height = val

    def area(self):
        """ Returns the area of a obj """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return(self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the obj"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
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

    def __repr__(self):
        """Returns a obj representation for eval()"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Delete function"""
        print("Bye rectangle...")
