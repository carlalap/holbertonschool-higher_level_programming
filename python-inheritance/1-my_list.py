#!/usr/bin/python3
"""
module 1. My list
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
