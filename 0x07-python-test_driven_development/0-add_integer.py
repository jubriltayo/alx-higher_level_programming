#!/usr/bin/python3
"""

Module containing function that adds two integers

"""


def add_integer(a, b=98):
    """ function that adds two integers or float and returns it

    Args:
        a: first argument
        b: second argument

    Return:
        Sum of two arguments

    Raises:
        TypeError: If arguments are not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
