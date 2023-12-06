#!/usr/bin/python3
"""
This module has a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file

    Args:
        filename (str, optional): text file. Defaults to "".
        search_string (str, optional): str to be searched for. Defaults to "".
        new_string (str, optional): new str to be written. Defaults to "".
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        for k, line in enumerate(lines):
            if search_string in line:
                lines[k] = line + new_string + "\n"
        f.seek(0)
        for line in lines:
            f.write(line)
