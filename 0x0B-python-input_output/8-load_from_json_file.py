#!/usr/bin/python3
"""Makes an object from a string from a file"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”:
    """
    with open(filename, "r") as fp:
        new_obj = json.load(fp)
    return new_obj
