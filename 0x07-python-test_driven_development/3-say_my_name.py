#!/usr/bin/python3
"""Prints a name
"""

def say_my_name(first_name, last_name=""):
    """say_my_name
    """
    if isinstance(first_name, str) == False:
        raise TypeError('first_name must be a string')
    elif isinstance(last_name, str) == False:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
