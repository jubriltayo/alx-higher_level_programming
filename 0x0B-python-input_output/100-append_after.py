#!/usr/bin/python3
"""Module that inserts a line of text to a file after
    each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line contain a
        specific string
    """
    new_text = ""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_text)
