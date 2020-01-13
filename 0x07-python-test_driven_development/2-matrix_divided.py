#!/usr/bin/python3
"""divides two lists in a matrix
"""
def matrix_divided(matrix, div):
    """ matrix_divided
    """
    if isinstance(div, (int, float)) == False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    ErrorType = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0 or isinstance(matrix, list) == False:
        raise TypeError(ErrorType)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(ErrorType)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if isinstance(value, (int, float)) == False:
                raise TypeError(ErrorType)
    MyArr = [round(value / div, 2) for value in row]
    return [MyArr for row in matrix]
