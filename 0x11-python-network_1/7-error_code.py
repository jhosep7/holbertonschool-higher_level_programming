#!/usr/bin/python3
""" send request """
from sys import argv
import requests

if __name__ == "__main__":
    R1 = requests.get(argv[1])
    R2 = R1.status_code
    print("Error code: {}".format(R2) if R2 > 400 else R1.text)
