#!/usr/bin/python3
"""
Note: This a an empty class Square that defines a square\
but does not have any function in it.

Args:
    size: is a private attribute of type int
"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
