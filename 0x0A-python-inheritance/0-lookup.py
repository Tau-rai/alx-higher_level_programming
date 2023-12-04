#!/usr/bin/python3
"""This module contains a function that prints the attributes of a class

"""


def lookup(obj):
    """
    A function that returns a list of available attrs and methods of an object

    Args:
        obj (class): a class object
    """
    return list(dir(obj))
