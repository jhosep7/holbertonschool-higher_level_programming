#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    else:
        my_listCPY = my_list.copy()
        my_listCPY[idx] = element
        return my_listCPY
