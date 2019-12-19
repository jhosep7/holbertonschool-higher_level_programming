#!/usr/bin/python3
def search_replace(my_list, search, replace):
    Put = [replace if Elem == search else Elem for Elem in my_list]
    return Put
