#!/usr/bin/python3
"""
This module contains a functions that writes text to a file
If the file doesnt exist it creates it, if it does it overrides
its contents and returns the number of chars added
"""


def append_write(filename="", text=""):
    """A function that writes text to a file

    Args:
        filename (str, optional): the text file. Defaults to "".
        text (str, optional): contents of the file. Defaults to "".
    Returns: the number of chars read
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
