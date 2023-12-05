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

    def to_json(self):
        """A method that retrieves the dict rep of a Student
        """
        return {key: value for key, value in self.__dict__.items()
                if type(value) in [list, dict, str, int, bool]}
