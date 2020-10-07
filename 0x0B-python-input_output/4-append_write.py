#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    opens a supplied file and appends text to the
    end of the file
    """
    count = 0

    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
    return count
