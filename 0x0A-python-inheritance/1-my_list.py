#!/usr/bin/python3
"""
This module contains a superclass and a subclass.
The MyList class inherits from the built-in list class
and adds a method to print a sorted version of the list.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    This class includes a method to print a sorted version of the list.
    """
    def print_sorted(self):
        """A function that prints a sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
