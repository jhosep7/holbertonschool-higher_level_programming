#!/usr/bin/python3
""" sends request to URL & displays the body of the response """
from urllib.error import URLError, HTTPError
from urllib import request, parse, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as Peer:
            print(Peer.read().decode('utf-8'))
    except URLError as ERRor:
        print("Error code: {}".format(ERRor.code))
