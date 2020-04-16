#!/usr/bin/python3
""" X-Request-Id """
from sys import argv
import requests

if __name__ == "__main__":
    Ans = requests.get(argv[1])
    print(Ans.headers.get('X-Request-Id'))
