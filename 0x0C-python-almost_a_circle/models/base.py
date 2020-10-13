#!/usr/bin/python3
"""A base class"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of 
        list_dictionaries, a list of dictionaries
        """
        if list_dictionaries is not None:
            if type(list_dictionaries) is list:
                if list_dictionaries == "":
                    return "[]"
                else:
                    return json.dumps(list_dictionaries)
        else:
            return "[]"
