#!/usr/bin/python3
""" Module that checks if object is instance
of a class
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class
    or inherited class directly or indirectly
    """
    return issubclass(type(obj), a_class) and a_class is not type(obj)
