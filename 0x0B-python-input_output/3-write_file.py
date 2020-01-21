#!/usr/bin/python3
"""function write string to a text file (UTF8) and returns characters written
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding="utf-8") as TheFile:
        return (TheFile.write(str(text)))
