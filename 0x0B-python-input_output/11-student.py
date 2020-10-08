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

    def to_json(self):
        """
        serializes the class object into json
        """
        return self.__dict__
