#!/usr/bin/python3
"""Module that contains subclass: Rectangle inherited
from class: Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines a subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints area of rectangle with '#' to stdout"""
        for i in range(self.area()):
            if i and (i % self.width == 0):
                print()
            print("#", end="")
        print()
        return ""
