#!/usr/bin/python3
"""Converting from string to obj with JSON"""
import json


def from_json_string(my_str):
    """
    Taking in a string and making an obj
    """
    return (json.loads(my_str))
