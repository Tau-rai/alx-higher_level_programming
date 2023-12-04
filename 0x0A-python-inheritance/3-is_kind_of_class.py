#!/usr/bin/python3
"""This module contains one function that checks fro an instance of class
"""


def is_kind_of_class(obj, a_class):
    """A function that checks for a class instance

    Args:
        obj (object): an instance of a class
        a_class (class): a class object
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
