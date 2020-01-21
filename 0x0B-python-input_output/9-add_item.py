#!/usr/bin/python3
import json
from sys import argv
""" script that adds all arguments to a Python list
"""


jsonSaved = __import__('7-save_to_json_file').save_to_json_file
jsonLoaded = __import__('8-load_from_json_file').load_from_json_file
filename = 'add_item.json'
try:
    NewFile = jsonLoaded(filename)
except (ValueError, FileNotFoundError):
    NewFile = []
NewFile += argv[1:]
jsonSaved(NewFile, filename)
