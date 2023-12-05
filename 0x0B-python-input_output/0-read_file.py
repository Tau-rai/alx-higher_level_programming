#!/usr/bin/python3
"""
This module contains a function that reads a text file
and prints it out to stdout
"""


def read_file(filename=""):
    """A function that reads a text file and prints it to stdout

    Args:
        filename (str): must be a text file containing strings. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
