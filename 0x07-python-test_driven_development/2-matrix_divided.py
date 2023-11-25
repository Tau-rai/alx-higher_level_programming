#!/usr/bin/python3
"""
A function that divides all elements of a matrix
Params: matrix and div(a number)
Returns a new matrix
Raises :
TypeError: if rows are not of the same size
TypeError: if div is not a number(int or float)
ZeroDivisionError: if div is equal to zero
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    Args:
        matrix (matrix): list of lists
        div (number): int or float
    """
    new_matrix = []
    row_len = len(matrix[0])

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for i in range(row_len):
            if not isinstance(row[i], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res = row[i] / div
            if res % 0.1 != 0:
                f_res = round(res, 2)
            else:
                f_res = round(res, 1)
            new_row.append(f_res)
        new_matrix.append(new_row)
    return new_matrix
