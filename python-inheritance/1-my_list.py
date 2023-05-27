#!/usr/bin/python3
class Mylist(list):
    """ Module: 1-my_list
    class Mylist inherit from list
    """

    def print_sorted(self):
        """prints ascending sort list """
        sorted_list = sorted(self)
        print(sorted_list)
