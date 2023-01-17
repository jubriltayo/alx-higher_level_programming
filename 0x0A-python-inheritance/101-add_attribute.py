#!/usr/bin/python3
"""Module that add new attribute to an object"""


def add_attribute(obj, attr, value):
    """Function that add new attribute to an object"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
