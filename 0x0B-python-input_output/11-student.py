#!/usr/bin/python3
"""
This module has a class Student
"""


class Student:
    """A class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """Instatiates attributes of class

        Args:
            first_name (str): name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that retrieves the dict rep of a Student
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs
                if attr in self.__dict__}

    def reload_from_json(self, json):
        """A method that replaces all attributes of the student instance

        Args:
            json (dict): a dictionary
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
