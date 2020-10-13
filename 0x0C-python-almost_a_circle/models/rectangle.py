#!/usr/bin/python3
"""Class Rectangle"""
from models import base
Base = base.Base


class Rectangle(Base):
    """
    Class rectanlge, inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an instance of rectangle
        param1: width, non-zero pos int
        param2: height, non-zero pos int
        param3: horzontal position, non-neg int
        param3: vertival position, non-neg int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    #Class functions
    def area(self):
        """
        Returns the area of a rectangle
        """
        return(self.__height * self.__width)

    def display(self):
        """
        Prints out a representation of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            for offset in range(self.__y):
                print()
            for rows in range(self.__height):
                for offset in range(self.__x):
                    print(" ", end="")
                for cols in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """
        Overrides the default str representation
        """
        i = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))

    def update(self, *args, **kwargs):
        """
        Fucntion to update a recatangle with ordered args
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        attrs = ["id", "width", "height", "x", "y"]
        if len(args) is not 0:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key in kwargs.keys():
                if key in attrs:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        returns a dictionary version of the object
        """
        rec_dict = {
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
            'id': self.id
        }
        return (rec_dict)

    #Getters and Setters
    @property
    def width(self):
        """
        Returns the value of the property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the attribute width
        param1: value must be non-zero pos int
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = int(value)

    @property
    def height(self):
        """
        returns the private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the attribute height
        param1: height must be non-zero pos int
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = int(value)

    @property
    def x(self):
        """
        returns the value of attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value of attribute x
        param1: x must be a non-neg int
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = int(value)

    @property
    def y(self):
        """
        returns the value of attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of attribute y
        param1: y must be a non-neg int
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = int(value)
