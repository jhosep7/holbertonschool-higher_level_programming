#!/usr/bin/python3
""" takes URL, sends request and displays value of X-Request-Id """
from urllib import request
import sys

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as Peer:
        print(Peer.getheader("X-Request-Id"))
