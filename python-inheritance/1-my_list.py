#!/usr/bin/python3
class Mylist(list):
    """
    MyList class inherits from list.
    
    This class provides an additional method, print_sorted,
    that prints the list in ascending order.
    """
    def __init__(self):
        """
        Initializes an instance of MyList.
        This constructor initializes the MyList object.
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in ascending order.
        This method sorts the list in ascending order using the sorted function
        and prints the sorted list.
        """
        sorted_list = sorted(self)
        print(sorted_list)
