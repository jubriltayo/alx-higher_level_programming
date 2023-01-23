#!/usr/bin/python3
"""Module that contains subclass: Rectangle inherited
from class: Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines a subclass"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not type(int):
            raise TypeError(self.__width + "must be an integer")
        if self.__width <= 0:
            raise ValueError(self.__width + "width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not type(int):
            raise TypeError(self.__height + "must be an integer")
        if self.__width <= 0:
            raise ValueError(self.__height + "height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__x < 0:
            raise ValueError(self.__x + "must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__y < 0:
            raise ValueError(self.__y + "must be >= 0")
        self.__y = y
