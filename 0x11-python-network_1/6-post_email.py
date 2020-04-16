#!/usr/bin/python3
""" send POST request """
from sys import argv
import requests

if __name__ == "__main__":
    Ans = requests.post(argv[1], {'email': argv[2]})
    print(Ans.text)
