#!/usr/bin/python3
""" script that fetches """
from urllib import request

with request.urlopen("https://intranet.hbtn.io/status") as Peer:
    Info = Peer.read()
    print("Body response:")
    print("\t- type: {}".format(type(Info)))
    print("\t- content: {}".format(Info))
    print("\t- utf8 content: {}".format(Info.decode(encoding="utf-8")))
