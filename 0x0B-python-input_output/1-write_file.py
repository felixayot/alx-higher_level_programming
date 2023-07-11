#!/usr/bin/python3
"""Defines a string write function to a text file."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the
       number of characters written:
    Args:
    filename(txt): file to be written
    text(str): string to be written to the filename
    Return:
    Number of characters written to filename
    """

    with open(filename, "w", encoding="utf-8") as text_file:
        return text_file.write(text)
