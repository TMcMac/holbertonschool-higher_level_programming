#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Read n lines from a file
    """
    line_count = 0
    with open(filename) as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end="")
                line_count += 1
        else:
            while line_count < nb_lines:
                line = f.readline()
                print(line, end="")
                line_count += 1
    return line_count
