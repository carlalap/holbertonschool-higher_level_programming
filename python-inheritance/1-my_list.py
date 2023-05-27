#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class Mylist(list):
    """Class inheriting from list class"""
    def print_sorted(self):
        """Public instance prints ascending sort list"""
        sorted_list = sorted(self)
        print(sorted_list)
