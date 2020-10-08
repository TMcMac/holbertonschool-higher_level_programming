#!/usr/bin/python3
"""This will get a line count on a text file"""


def number_of_lines(filename=""):
    """
    A function to get a line count on a file
    parameters - a file
    """
    line_count = 0
    with open(filename, 'r') as f:
        """
        Opens the file as f in such as way that
        we don't need to worry about f.close()
        """
        for line in f:
            """
            we'll loop through the file one list at a time
            """
            line_count += 1

    return line_count
