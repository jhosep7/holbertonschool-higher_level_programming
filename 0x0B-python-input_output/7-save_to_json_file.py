#!/usr/bin/python3
import json
"""function that writes an Object to a text file, using a JSON
"""


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w') as TheFile:
        json.dump(my_obj, TheFile)
