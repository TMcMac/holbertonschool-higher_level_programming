#!/usr/bin/python3
"""Defines class square and takes in a size to intialize square"""


class Square():
    """A basic class of a square that will take in size
    which must be an int and will be used for both height
    and for the width of the square as they are equal"""
    def __init__(self, size=0, position=(0, 0)):
        """When you initialize a square
         Args:
            size (int): Height x Width of the square
            position (tuple): x/y offset position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Just returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """When you set size of a square, check that size is an
        int and if so set its size else raise an error"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retruns the current set position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the Area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints out the square using #'s """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    for k in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
