#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_set = set()
    for thing in set_1:
        if thing in set_2:
            new_set.add(thing)
    return new_set
