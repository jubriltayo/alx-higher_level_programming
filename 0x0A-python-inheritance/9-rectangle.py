#!/usr/bin/python3
""" Module to create a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a subclass: Rectangle """
    def __init__(self, width, height):
        """ Initializes an instance of the class """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Prints string"""
        a = str(self.__width)
        b = str(self.__height)
        return "[Rectangle] " + a + "/" + b
