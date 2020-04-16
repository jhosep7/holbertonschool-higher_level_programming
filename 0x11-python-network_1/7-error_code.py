#!/usr/bin/python3
""" send request """
from sys import argv
import requests

if __name__ == "__main__":
    R1 = requests.get(argv[1])
    code = R1.status_code
    print("Error code: {}".format(code) if code > 400 else R1.text)
