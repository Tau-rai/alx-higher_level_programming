#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    def __str__(self):
        """
        A function that prints a rectangle of # character

        Returns:
            str: string respresentation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return "\n".join('#' * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        This method returns a string representation
        Returns:
            str: string respresentation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
