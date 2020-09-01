#!/usr/bin/python3
def uppercase(str):
    new_str = []
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            new_str.append(chr(ord(c) - 32))
        else:
            new_str.append(c)
    print("{}".format(''.join(new_str)))
