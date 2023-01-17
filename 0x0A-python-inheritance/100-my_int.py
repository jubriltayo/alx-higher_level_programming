#!/usr/bin/python3
"""Module that creates a class"""


class MyInt(int):
    """Defines a subclass: MyInt"""
    def __eq__(self, other):
        """Returns a not equal operator"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Returns an equal operator"""
        return int.__eq__(self, other)
