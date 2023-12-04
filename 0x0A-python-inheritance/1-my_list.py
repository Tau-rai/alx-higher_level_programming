#!/usr/bin/python3
"""
This module contains a superclass and a subclass
"""


class MyList(list):
    """A class that inherits from the list class
    """
    def print_sorted(self):
        """A function that prints a sorted list
        """
        sort_list = sorted(self)
        print(sort_list)
