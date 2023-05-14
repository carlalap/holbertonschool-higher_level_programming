#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_list = list(set_1) + list(set_2)
    n_list = []

    for i in range(len(set_list)):
        if set_list.count(set_list[i]) > 1:
            n_list.append(set_list[i])
    return set(n_list)
