#!/usr/bin/python3
"""Reading out N lines from text doc"""


def read_lines(filename="", nb_lines=0):
    """
    A function to read n lines of a file
    parameters - filename: a file
                 nb_lines (int): number of lines
    """
    line_count = 0
    with open(filename, 'r') as f:
        """
        opens the file safely in readmode
        """
        if nb_lines > 0:
            while line_count < nb_lines:
                """
                reading out 1 line at a time
                """
                line = f.readline()
                print(line, end="")
                line_count += 1
        elif nb_lines == 0:
            for line in f:
                print(line, end="")
                line_count += 1
    return line_count
