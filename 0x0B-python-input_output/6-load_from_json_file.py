#!/usr/bin/python3
"""
This module has a function that creates an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a JSON file

    Args:
        filename (str): a python object
    """
    with open(filename, "r") as f:
        return json.load(f)
