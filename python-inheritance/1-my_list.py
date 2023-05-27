#!/usr/bin/python3
""" Module: 1-my_list
    class Mylist inherit from list"""

class Mylist(list):
    """
    Class Mylist inherits list
    """

    def print_sorted(self):
        """prints ascending sort list """

        sorted_list = sorted(self)
        print(sorted_list)
