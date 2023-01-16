#!/usr/bin/python3
""" Module to create a subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a subclass: Square """
    def __init__(self, size):
        """ Initializes an instance of the class """
        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Returns the area of a square"""
        return pow(self.__size, 2)

    def __str__(self):
        """Prints string"""
        a = str(self.__size)
        return "[Square] " + a + "/" + a
