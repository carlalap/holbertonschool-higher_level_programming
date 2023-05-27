#!/usr/bin/python3
"""
module 1. My list
"""

class Mylist(list):
    """
    MyList class inherits from list.

    This class provides an additional method, print_sorted,
    that prints the list in ascending order.
    """
    def print_sorted(self):
        print(sorted(self))
