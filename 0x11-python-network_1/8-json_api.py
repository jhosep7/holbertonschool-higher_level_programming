#!/usr/bin/python3
""" takes in a letter and sends a POST """
from sys import argv
import requests

if __name__ == "__main__":
    q = argv[1] if len(argv) > 1 else ""
    try:
        R1 = requests.post('http://0.0.0.0:5000/search_user',
                           data={'q': q}).json()
        print("[{}] {}".format(R1['id'], R1['name'])
              if 'id' in R1 and 'name' in R1 else "No result")
    except ValueError:
        print("Not a valid JSON")
