#!/usr/bin/python3
"""Class to json without importing"""


class Student:
    """
    Basic in formation about a student
    """
    def __init__(self, first_name="", last_name="", age=0):
        """
        Initializes a student object
        inputs: first_name - a string
                last_name - a string
                age - an integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        serializes the class object into json
        """
        if type(attrs) is not list or attrs == None:
            return (self.__dict__)
        else:
            new_dict = {}
            for key in self.__dict__:
                """
                Cycling through the keys
                """
                for match in attrs:
                    if key == match:
                        new_dict[key] = self.__dict__[key]
            return new_dict
