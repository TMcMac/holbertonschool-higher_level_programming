#!/usr/bin/env python3
def remove_char_at(str, n):
    new_str = ""
    for i in range(0, len(str)):
        if i != n:
            new_str += str[i]
        else:
            pass
    return new_str
