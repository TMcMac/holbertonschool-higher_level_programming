#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for char in my_string:
        if char is 'c':
            pass
        elif char is 'C':
            pass
        else:
            new_string.append(char)

    return (''.join(new_string))
