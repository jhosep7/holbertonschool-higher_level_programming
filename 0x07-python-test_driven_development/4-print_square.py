#!/usr/bin/python3
"""Print a square
"""
def print_square(size):
    if isinstance(size, int) == False:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print("{}\n".format("#" * size) * size, end='')
