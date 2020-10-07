#!/usr/bin/python3
"""Docstring, not sure what this is for"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of class
    parameters - obj: an object to be compared
                 a_class: a class
    """
    if (type(obj) == a_class):
        return(True)
    else:
        return(False)
