#!/usr/bin/python3
"""Docstring what do you do?"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of class or inherited class
    parameters - obj: an object
                 a_class: a class
    """
    return(isinstance(obj, a_class))
