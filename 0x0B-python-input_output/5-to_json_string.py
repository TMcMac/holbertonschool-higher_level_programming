#!/usr/bin/python3
"""Using JSON to output a string"""

import json


def to_json_string(my_obj):
    """
    Take in an object and output a string
    parameters - my_obj (an object)
    """

    return (json.dumps(my_obj))
