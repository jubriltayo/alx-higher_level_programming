#!/usr/bin/python3
"""Module that creates an inherited class"""


class MyList(list):
    """creates a child class (MyList) that inherits from list """

    def print_sorted(self):
        """ Prints sorted list in ascending order """
        print(sorted(self))
        return sorted(self)
