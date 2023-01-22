#!/usr/bin/python3
"""Module that creates class: Student"""


class Student:
    """Defines a class: Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dict representation of an instance
of a class: Student
        """
        return self.__dict__
