#!/usr/bin/python3
"""Pascal's Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return ([])
    if n == 1:
        return ([[1]])
    Line = [[1 for j in range(i + 1)]for i in range(n)]
    for n in range(0, n):
        for i in range(0, n - 1):
            Line[n][i + 1] = sum(Line[n - 1][i:i + 2])
    return (Line)
