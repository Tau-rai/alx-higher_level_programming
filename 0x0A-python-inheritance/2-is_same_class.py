#!/usr/bin/python3
"""This module contains one function that checks fro an instance of class
"""


def is_same_class(obj, a_class):
    """A function that checks for a class instance

    Args:
        obj (object): an instance of a class
        a_class (class): a class object
    """
    return type(obj) is a_class
