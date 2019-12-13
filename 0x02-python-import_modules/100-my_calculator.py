#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    Sign = argv[2]
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if Sign != "+" and Sign != "-" and Sign != "*" and Sign != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        if argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        if argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        if argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            exit(0)
