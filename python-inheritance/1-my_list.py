#!/usr/bin/python3

class Mylist(list):
    """Class inheriting from list class"""
    def print_sorted(self):
        """Public instance prints the list, but sorted (ascending sort)"""
        sorted_list = sorted(self)
        print(sorted_list)
