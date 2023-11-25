#!/usr/bin/python3
"""
A function that prints a formatted string
Args:
        first_name (str): must be a string
        last_name (str, optional): must be string. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
Returns: Nothing
"""


def say_my_name(first_name, last_name=""):
    """_
    A function that prints a formatted string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        raise ValueError("first_name can not be empty")
    print("My name is", first_name, last_name)
