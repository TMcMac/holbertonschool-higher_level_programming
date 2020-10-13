#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle(Base):
    """
    Class rectanlge, inherits from base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes an instance of rectangle
        param1: width, non-neg int
        param2: height, non-neg int
        param3: horzontal position, non-neg int
        param3: vertival position, non-neg int
        """
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
            param1: value must be non-neg int
            """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            elif value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

        
