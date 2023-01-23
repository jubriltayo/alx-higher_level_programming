#!/usr/bin/python3
"""Module that creates a child class which inherits
from class: Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a child class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string"""
        name = str("[Square] ")
        i = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        return (name + "(" + i + ") " + x + "/" + y + " - " + w)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates class with addition of attributes
        using args(ints) and kwargs(dict - key/value pair)
        """
        count = 1
        if args and len(args):
            for arg in args:
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.size = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of class"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
