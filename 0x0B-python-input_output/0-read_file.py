#!/usr/bin/python3
def read_file(filename=""):
    """
    open a file using with and print to stdout
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
