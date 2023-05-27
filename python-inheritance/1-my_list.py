#!/usr/bin/python3
class Mylist(list):
    """
    Class Mylist inheriting from list
    """

    def print_sorted(self):
        """prints ascending sort list """
        sorted_list = sorted(self)
        print(sorted_list)
