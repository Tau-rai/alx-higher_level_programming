#!/usr/bin/python3
"""
This module has a function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """A function that returns an object rep of a JSON string

    Args:
        my_str (json): a JSON string
    Returns:
        an object (python data structure)
    """
    return json.loads(my_str)
