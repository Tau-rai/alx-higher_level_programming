#!/usr/bin/python3
"""
A function that prints a square with the character #

Args:
    size (int): length of the square
"""


def print_square(size):
    """
    A function that prints a square with the character #
    """
    if not isinstance(size, int):
        raise TimeoutError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("must be an integer")
    if size == 0:
        print("")
    else:
        for k in range(size):
            print('#' * size)
