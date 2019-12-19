#!/usr/bin/python3
def weight_average(my_list=[]):
    AnsMUL = sum([x * y for x, y in my_list])
    AnsDIV = sum(y for x, y in my_list)
    return (AnsMUL/AnsDIV)
