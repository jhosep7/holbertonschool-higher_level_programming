#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    VarAdd = 0
    for i in range(1, argc):
        VarAdd += int(argv[i])
    print("{:d}".format(VarAdd))
