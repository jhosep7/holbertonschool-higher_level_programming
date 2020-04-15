#!/usr/bin/python3
""" sends a POST request to the passed URL """
from urllib import request, parse
import sys

if __name__ == "__main__":
    Info = parse.urlencode({'email': sys.argv[2]}).encode()
    with request.urlopen(sys.argv[1], Info) as Peer:
        print(Peer.read().decode('utf-8'))
