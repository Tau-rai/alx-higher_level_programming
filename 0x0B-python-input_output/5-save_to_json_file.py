#!/usr/bin/python3
"""
This module has a function that writes an Object to a text file,
using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file

    Args:
        my_obj (json): a json string
        filename (text file): a python object
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
