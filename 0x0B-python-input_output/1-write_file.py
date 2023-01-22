#!/usr/bin/python3
"""Module that writes a string into a file"""


def write_file(filename="", text=""):
    """Writes a string into a file and returns
the number of characters
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
