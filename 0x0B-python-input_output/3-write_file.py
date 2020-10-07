#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Writing a string of text in UTF8 to a file
    parameters - filename(file): a file for output
                 text (string): text to be written
    """
    with open(filename, mode="w+", encoding="utf-8") as w:
        """
        opens the file in write mode safely with utf-8 encoding
        """
        w_count = w.write(text)
    return w_count
