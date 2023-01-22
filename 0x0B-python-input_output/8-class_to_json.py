#!/usr/bin/python3
"""Module that returns dictionary description 
with simple data structure (list, dict, str, int
and boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns dictionary description of an object"""
    return obj.__dict__
