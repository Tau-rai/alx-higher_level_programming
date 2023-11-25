#!/usr/bin/python3
"""
A function that adds two integers a & b
Returns: int: sum of a and b.
Raises: TypeError: if either a or b is not an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers together
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
