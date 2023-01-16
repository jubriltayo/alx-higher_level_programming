#!/usr/bin/python3
""" Module that checks if object is instance
of a class
"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance of class"""
    return type(obj) is a_class
