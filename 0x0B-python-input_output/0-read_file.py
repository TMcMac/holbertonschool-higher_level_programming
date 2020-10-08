#!/usr/bin/python3
"""Reads a text filr to stdout"""


def read_file(filename=""):
    """
    This function reads a text file to
    StdOut
    parameters - filename (file): the file to be read
    """
    with open(filename, 'r') as f:
        """
        Opens the file in such a way that it will be
        closed whenever function ends
        """
        for line in f:
            """
            reading through each line in file
            """
            print(line, end="")
