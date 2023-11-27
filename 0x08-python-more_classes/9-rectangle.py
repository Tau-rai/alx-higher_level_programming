#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
            output = []
            symbol = str(self.print_symbol)
            for _ in range(self.__height):
                output.append(symbol * self.__width)
            return "\n".join(output)

    def __repr__(self):
        """
        This method returns a string representation
        Returns:
            str: string respresentation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Trcaks the deletion of an instance of a Rectangle
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two rectangles and returns the biggest
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        creates a square as an intance of the Rectablge class
        """
        return cls(width=size, height=size)
