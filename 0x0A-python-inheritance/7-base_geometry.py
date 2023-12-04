#!/usr/bin/python3
"""T
his module contains a Geometry class
"""


class BaseGeometry:
    """
    A geometry class
    """
    def area(self):
        """A function that calculates area
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
