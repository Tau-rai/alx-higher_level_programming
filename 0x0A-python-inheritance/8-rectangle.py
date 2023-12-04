#!/usr/bin/python3
"""
This module contains a class that inherits from the BaseGeometry class
the subclasses are Rectangle and Square
"""


class BaseGeometry:
    """
    A geometry super class with two subclasses
    and use two methods one that calculates area and a validator
    """
    def area(self):
        """
        A function that calculates area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates the value

        Args:
            name (string): variable name of the value
            value (int): an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A subclass of the Geometry class

    Args:
        BaseGeometry (class): A mathematical computations class
    """
    def __init__(self, width, height):
        """instatiation of the Rectangle class

        Args:
            width (int): an integr
            height (int): an integer
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
