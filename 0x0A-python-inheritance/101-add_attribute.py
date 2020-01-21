#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible
"""


def add_attribute(MyObject, MyAttr, MyValue):
    if hasattr(MyObject, "__dict__"):
        setattr(MyObject, MyAttr, MyValue)
    else:
        raise TypeError("can't add new attribute")
