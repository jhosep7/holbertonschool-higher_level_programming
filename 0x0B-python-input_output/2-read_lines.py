#!/usr/bin/python3
"""reads n lines of a text file (UTF8) and prints it to stdout:
"""


def read_lines(filename="", nb_lines=0):
    counter = 0
    with open(filename, mode='r', encoding="utf-8") as TheFile:
        for line in TheFile:
                counter += 1
                print(line, end='')
                if nb_lines == counter:
                    break
