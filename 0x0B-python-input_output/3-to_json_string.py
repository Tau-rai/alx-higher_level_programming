#!/usr/bin/python3
"""
This module has a function that returns json format of a string
"""


import json


def to_json_string(my_obj):
    """A function that returns the JSON rep of an object

    Args:
        my_obj (str): a string object
    Returns:
        json representation of an object
    """
    return json.dumps(my_obj)
