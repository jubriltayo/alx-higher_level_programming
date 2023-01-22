#!/usr/bin/python3
"""Module to read file and prints it to stdout"""
import json


def read_file(filename=""):
    """Reads content of a file and prints"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
