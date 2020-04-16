#!/usr/bin/python3
""" 7-error_code.py """
import requests
from sys import argv


if __name__ == "__main__":
    R1 = requests.get(argv[1])
    code = R1.status_code
    if code > 400:
        print("Error code: {}".format(code))
    else:
        print(reply.text)
