#!/usr/bin/python3
"""
Note: This a an empty class Square that defines a square\
and has one function in it.

Args:
    size: is a private attribute of type int
"""


class Square:
    """This is a class that define a square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """This is a function that calculates area given the size"""
        return int(self.__size) ** 2
