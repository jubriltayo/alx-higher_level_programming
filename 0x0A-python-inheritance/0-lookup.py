#!/usr/bin/python3
""" Module that checks available attributes
and methods of an object
"""


def lookup(obj):
    """Returns list of attributes and methods"""
    return dir(obj)
