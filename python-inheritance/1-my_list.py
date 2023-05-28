#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Class Mylist inherits list"""

    def print_sorted(self):
        """
        prints the list, but sorted
        """
        print(sorted(self))
