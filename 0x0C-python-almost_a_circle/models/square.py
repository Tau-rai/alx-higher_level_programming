#!/usr/bin/python3
"""
This module contains a class Square that inherits from the class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is class that inherits from the Rectangle class

    Args:
        Rectangle (class): a super class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instatiation of the class
        Args:
            size (int): size of the square
            x (int, optional): an integer. Defaults to 0.
            y (int, optional): an integer. Defaults to 0.
            id (_type_, optional): an integer. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self) -> str:
        """A method that returns a str representation of the square

        Returns:
            str: a string rep of square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {super().width}"

    def update(self, *args, **kwargs):
        """A method that assigns arguments to each attribute
        Args:
            *args: sequence of values to assign to the square's attrs
            **kwargs: a dict of attr names and values to assign to Square attrs
        """
        attributes = ["id", "size", "x", "y"]
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square
        """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
