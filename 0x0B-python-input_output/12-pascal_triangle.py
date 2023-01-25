#!/usr/bin/python3
"""Module that returns Pascal's triangle"""


def pascal_triangle(n):
    """Returns list of list of integers representing
        the Pascal's triangle
    """
    outer_list = []
    if n <= 0:
        return outer_list

    for line in range(n):
        inner_list = []
        for i in range(line + 1):
            if (i == 0) or (i == line):
                res = 1
            else:
                res = outer_list[line - 1][i] + outer_list[line - 1][i - 1]
            inner_list.append(res)
        outer_list.append(inner_list)
    return outer_list
