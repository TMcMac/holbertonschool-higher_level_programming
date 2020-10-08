#!/usr/bin/python3
"""Now appending text to a file"""


def append_write(filename="", text=""):
    """
    This function will append text to a file
    parameters - filename(file): destination file
                 text(string): to be appended to file
    """
    with open(filename, mode="a+", encoding="utf-8") as a:
        """
        Safe open in append mode
        """
        return a.write(text)
