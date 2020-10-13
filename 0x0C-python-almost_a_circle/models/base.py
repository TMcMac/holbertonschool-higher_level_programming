#!/usr/bin/python3
"""A base class"""


class Base():
    """
    This is the base class for this project
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        This initializes an object of type base
        param1 = id, an int, or if none set to nb_object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
