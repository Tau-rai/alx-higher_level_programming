#!/usr/bin/python3
"""
Note: This a an empty class Square that defines a square\
and has two functions in it. area() and my_print()

Args:
    size: is a private attribute of type int
"""


class Square:
    """This is a class that define a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @size.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(k, int) and k >= 0 for k in value):
                self.__position = value
            else:
                raise ValueError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """This is a function that calculates area given the size"""
        return int(self.__size) ** 2

    def my_print(self):
        """This functions prints in stdout the square with the charcter #"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + '#' * self.__size for _ in range(self.__size)))
