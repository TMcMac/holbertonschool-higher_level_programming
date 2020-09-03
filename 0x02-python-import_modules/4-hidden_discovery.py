#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)
    names.sort()
    for name in names:
        if '__' not in name:
            print(name)
