#!/usr/bin/python3
"""
This module has a function that returns dict description with
a simple data structure for JSON serialization
"""


def class_to_json(obj):
    """A function that returns the dcit description with simple data struct

    Args:
        obj (any): a simple data structure
    """
    dat_types = (list, dict, str, int, bool)
    filter_dict = {key: value for key, value in obj.__dict__.items()
                   if type(value) in dat_types}
    return filter_dict
