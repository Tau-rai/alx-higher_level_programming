#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from the class Base
"""


from models.base import Base


class Rectangle(Base):
    """This is class that inherits from the Base class

    Args:
        Base (class): a super class
    """
    char_sym = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instatiation of the class
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): an integer. Defaults to 0.
            y (int, optional): an integer. Defaults to 0.
            id (_type_, optional): an integer. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        A method that calculates teh area of the Rectange
        """
        return self.__width * self.__height

    def display(self):
        """A method that displays the rectangle with # characters
        """
        output = []
        symbol = str(self.char_sym)
        for _ in range(self.__y):
            output.append(" " * self.__x)
        for _ in range(self.__height):
            output.append(" " * self.__x + symbol * self.__width)
        print("\n".join(output))

    def __str__(self) -> str:
        """A method that returns a str rep of the output

        Returns:
            str: string representation of the output
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """A method that assigns arguments to each attribute
        Args:
            *args: sequence of values to assign to the rectangle's attrs
            **kwargs: a dict of attr names and values to assign to Rect attrs
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
