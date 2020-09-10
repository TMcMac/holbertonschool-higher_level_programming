#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for n, i in enumerate(new_list):
        if i == search:
            new_list[n] = replace
    return new_list
