#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for String in sorted(a_dictionary.keys()):
        print("{}: {}".format(String, a_dictionary[String]))
