#!/usr/bin/python3
"""
This module contanins a class Base
"""


import json
import os
import csv


class Base:
    """This is a class with private attributes and a constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instatiation of the class Base

        Args:
            id (int, optional): an integr. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON str representation of list_dictionaries

        Args:
            list_dictionaries (dict): a list of dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON to str representation of list_objs

        Args:
            list_objs (list): a list of instances who inherits of Base
        """
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON str representation

        Args:
            json_string (str): string representing a list of dicts
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary: a dict of attr names and values
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        # set real attribute values using the update method
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        """
        file = cls.__name__ + ".json"

        if not os.path.exists(file):
            return []
        # read file and create instances
        with open(file, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**dict_) for dict_ in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes dict onjects to csv file

        Args:
            list_objs (list): a list of python objects
        """
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csvfile:
            if list_objs is not None and len(list_objs) > 0:
                fields = list_objs[0].to_dictionary().keys()
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of objs
        """
        filename = cls.__name__ + ".csv"
        list_objs = []
        try:
            with open(filename, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)

                    list_objs.append(cls.create(**row))
        except FileNotFoundError:
            pass
        return list_objs
