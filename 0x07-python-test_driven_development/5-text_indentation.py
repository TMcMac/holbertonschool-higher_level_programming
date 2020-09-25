#!/usr/bin/python3
""" A function to break up a sting in to lines based in . and ? """


def text_indentation(text):
    """
    text_indentation - will break a string into new lines each time
    it enounters a . or ?
    Argument1 - a string
    return - none but prints to stdout
    """
    flag = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if flag == 1:
            print()
            print()
        if text[i] is ' ' and text[i - 1] in [".", "?", ":"]:
            pass
        else:
            print("{}".format(text[i]), end="")
        flag = 0
        if text[i] in [".", "?", ":"]:
            flag = 1
