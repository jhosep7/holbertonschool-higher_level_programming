#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    with open(filename, mode='r', encoding="utf-8") as TheFile:
        for line in TheFile:
            print(line, end='')
