#!/usr/bin/python3
"""script that fetches"""
import requests

if __name__ == "__main__":
    Ans = requests.get ('https://intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(Ans)))
    print("\t- content: {}:".format(Ans))
