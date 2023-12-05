#!/usr/bin/python3
"""
This module contains a function that adds an attribute to a class
if not possible it raises a TypeError
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if its possible

    Args:
        obj (class): an object
        attr (attr): attribute to be added
        value (any): any type
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
