#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if my_list is None:
        return
    my_list2 = []

    for i in my_list:
        if i is search:
            my_list2.append(replace)
        else:
            my_list2.append(i)
    return my_list2
