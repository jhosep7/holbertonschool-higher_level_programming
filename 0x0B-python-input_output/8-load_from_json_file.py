#!/usr/bin/python3
import json
"""Crate an object from a json file
"""


def load_from_json_file(filename):
    with open(filename) as TheFile:
        NewObj = json.load(TheFile)
    return NewObj
