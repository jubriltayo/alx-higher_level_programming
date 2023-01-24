#!/usr/bin/python3
"""Module that creates class: Student"""


class Student:
    """Defines a class: Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dict representation of an instance
of a class: Student
        """
        if (type(attrs) == list and all(type(element) == str for
                                        element in attrs)):
            return {key: getattr(self, key) for key in attrs if
                    hasattr(self, key)}
        return self.__dict__
