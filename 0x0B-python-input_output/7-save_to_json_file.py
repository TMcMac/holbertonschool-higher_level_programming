#!/usr/bin/python3
"""Write obj to text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file,
    using a JSON representation
    parameters - my_obj (object)
                 filename (file): destination for output
    """
    with open(filename, "w+") as fp:
        """
        Safe opens or creates file in write mode
        """
        json.dump(my_obj, fp)
