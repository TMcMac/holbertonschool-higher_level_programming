#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    i = 0
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    while i < len(sys.argv):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
        i += 1
