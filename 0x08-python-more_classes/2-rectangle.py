#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """A function that calculates area of the rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def perimeter(self):
        """A function that calculates perimeter of a rectangle

        Returns:
            int: perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perim = (2 * self.__width) + (2 * self.__height)
            return perim
