#!/usr/bin/python3
""" Module to create a class"""


class BaseGeometry:
    """ Defines class BaseGeometry"""
    def area(self):
        """ Returns the area"""
        raise Exception("area() is not implemented")
