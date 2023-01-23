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
        x_axis = self.x
        y_axis = self.y
        for i in range(y_axis):
            print()
        for i in range(self.area()):
            if i and (i % self.width == 0):
                print()
            if not (i % self.width):
                for j in range(x_axis):
                    print(" ", end="")
            print("#", end="")
        print()

    def __str__(self):
        """Prints to stdout"""
        name = "[Rectangle] "
        i = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        h = str(self.height)
        return (name + "(" + i + ") " + x + "/" + y + " - " + w + "/" + h)

    def update(self, *args):
        """Updates class with addition of attributes
        using args
        """
        count = 1
        if args and len(args):
            for arg in args:
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.width = arg
                elif count == 3:
                    self.height = arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
                count += 1
