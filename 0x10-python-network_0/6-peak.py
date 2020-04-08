#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    arr = list_of_integers
    if not list_of_integers:
        return None
    """if len(list_of_integers) >= 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] > list_of_integers[-2]:
            return list_of_integers[n-1]"""
    for i in range(len(arr)):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return list_of_integers[0]
