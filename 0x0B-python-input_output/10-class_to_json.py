#!/usr/bin/python3
"""Get a simply dict() fromt serialized JSON"""


def class_to_json(obj):
    """
    Takes in an obj and reutrns a dict
    """
    return obj.__dict__
