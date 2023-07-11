#!/usr/bin/python3
"""Defines a text file reader."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:
    Args:
    filename(txt): the file to be read
    """

    with open(filename, encoding="utf-8") as read_data:
        print(read_data.read(), end="")
