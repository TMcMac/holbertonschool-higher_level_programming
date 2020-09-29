#!/usr/bin/python3
"""A definition of a class"""


class Rectangle():
    """
    A class for foursided polygons
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize an object of class rectangle
        Param1: the width, >=0, must be an int
        Param2: the height, >=0, must be an int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    obj_str += Rectangle.print_symbol
                obj_str += '\n'
            obj_str = obj_str[:-1]
            return obj_str

    def __repr__(self):
        """Returns a obj representation for eval()"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """Delete function"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """
        Function to compare two instances of rectangle
        Param1: an instance of Rectangle
        Param2: a second instance of Rectangle
        Return: The larger of the two
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        r_1 = rect_1.area()
        r_2 = rect_2.area()
        if r_1 > r_2:
            return rect_1
        elif r_1 < r_2:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """makes a square of a rectangle"""
        return Rectangle(size, size)
