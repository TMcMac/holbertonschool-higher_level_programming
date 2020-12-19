#!/usr/bin/python3
"""A simple python script to find peaks in an unsorted array"""


def find_peak(list_of_integers):
    """Fine a peak in an unsorted list"""
    peaks = []
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        return max(list_of_integers)
