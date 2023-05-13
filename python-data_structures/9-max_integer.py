#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    my_list.sort()
    n = len(my_list)
    max_value = my_list[n - 1]
    return (max_value)
