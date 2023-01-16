#!/usr/bin/python3
""" Module that checks if object is instance
of a class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of a class
    or inherited class
    """
    return isinstance(obj, a_class)
