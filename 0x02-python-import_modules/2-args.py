#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc < 2:
        print("{:d} arguments.".format(argc - 1))
    else:
        if argc == 2:
            print("{:d} argument:".format(argc -1))
        else:
            print("{:d} arguments:".format(argc -1))
    for i in range(1, argc):
        print("{:d}: {:s}".format(i, argv[i]))
