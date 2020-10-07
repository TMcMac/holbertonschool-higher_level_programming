#!/usr/bin/python3
"""Docstring"""


class MyList(list):
    """
    Inherites from list
    """
    def print_sorted(self):
        """
        prints a sorted list
        parameters - only self
        """
        sorted_list = sorted(self)
        print(sorted_list)
