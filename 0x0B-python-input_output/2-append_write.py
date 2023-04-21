#!/usr/bin/python3
"""
contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """Function that appends text to a file

    Args:
    filename: filename
    text: text to write

    Raises
    Exception: When file can be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
