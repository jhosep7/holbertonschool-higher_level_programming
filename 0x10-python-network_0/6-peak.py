#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ finding the peak """
    arr = list_of_integers
    if not list_of_integers:
        return None
    for i in range(len(arr)):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return list_of_integers[0]
