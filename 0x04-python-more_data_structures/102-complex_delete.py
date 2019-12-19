#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for Key in list(a_dictionary.keys()):
        if a_dictionary[Key] == value:
            del a_dictionary[Key]
    return a_dictionary
