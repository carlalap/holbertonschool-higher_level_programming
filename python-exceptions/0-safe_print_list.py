#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    try:
        n = 0
        for i in my_list:
            if n < x:
                print("{}".format(i), end='')
                n = n + 1
        print('')
        return n
    except IndexError:
        print("Index Not Match")
