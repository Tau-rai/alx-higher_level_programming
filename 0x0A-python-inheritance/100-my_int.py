#!/usr/bin/python3
"""
This module contains a class that inherits from the inbuilt int class
Inverts comparison operators
"""


class MyInt(int):
    """a class that inherits from the int super class

    Args:
        int (class): the inbuilt int class
    """
    def __eq__(self, other) -> bool:
        """Inverts the == operator

        Returns:
            bool: false
        """
        return int.__ne__(self, other)

    def __ne__(self, other) -> bool:
        """Inverts the != operator

        Returns:
            bool: true
        """
        return int.__eq__(self, other)
