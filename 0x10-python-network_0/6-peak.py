#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ finding the peak """
    arr = list_of_integers
    if not arr:
        return None
    if len(arr) > 1:
        if arr[0] >= arr[1]:
            return arr[0]
        if arr[-1] >= arr[-2]:
            return arr[-1]
        for i in range(len(arr)):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return arr[i]
    return arr[0]
