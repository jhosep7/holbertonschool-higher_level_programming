#!/usr/bin/python3
"""function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    counter = 0
    with open(filename, mode='r', encoding="utf-8") as TheFile:
        for line in TheFile:
            counter += 1
    return (counter)
