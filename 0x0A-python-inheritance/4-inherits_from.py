#!/usr/bin/python3
"""Docstring for lookup"""


def inherits_from(obj, a_class):
    """
    Checks to see if an obj is a instance of a subclass
    parameters - obj: an object
                 a_class: a class
    """
    if (type(obj) == a_class):
        return False
    elif (issubclass(type(obj), a_class)):
        return True
    else:
        return False
