#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as TheError:
        stderr.write("Exception: {}\n".format(TheError))
        return (None)
