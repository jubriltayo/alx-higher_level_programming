#!/usr/bin/python3
"""Module to create a class: Base"""
import json


class Base:
    """Defines class: Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string to a file"""
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding="utf-8") as f:
            if not list_objs:
                result = []
            else:
                result = [i.to_dictionary() for i in list_objs]
            f.write(Base.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes"""
        if cls.__name__ == 'Rectangle':
            shape = cls(1, 1)
        else:
            shape = cls(1)
        shape.update(**dictionary)
        return shape
