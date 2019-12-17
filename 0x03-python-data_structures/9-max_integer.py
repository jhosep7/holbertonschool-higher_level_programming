#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    CopyList = my_list.copy()
    CopyList.sort()
    return CopyList[-1]
