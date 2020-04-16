#!/usr/bin/python3
""" takes your Github credentials """
from sys import argv
import requests

if __name__ == "__main__":
    Id = requests.get('https://api.github.com/user',
                      auth=(argv[1], argv[2])).json()
    print(Id['id'] if "id" in Id else None)
