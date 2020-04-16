#!/usr/bin/python3
""" Github commits """
from sys import argv
import requests


if __name__ == "__main__":
    R1 = requests.get('https://api.github.com/repos/{}/{}/commits'
                      .format(argv[2], argv[1])).json()
    i = 0
    for j in R1:
        if i < 10:
            Sh = j.get("sha")
            Auth = j.get("commit").get("author").get("name")
            print("{}: {}".format(Sh, Auth))
        i += 1
