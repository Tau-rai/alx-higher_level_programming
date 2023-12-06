#!/usr/bin/python3
"""
This module has a Pascal triangle function
"""


def pascal_triangle(n):
    """A function that implements the Pascal's triangle

    Args:
        n (int): an integer
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for k in range(1, n):
        row = [1]
        l_row = triangle[-1]
        row += [l_row[j] + l_row[j+1] for j in
                range(len(l_row) - 1)]
        row.append(1)
        triangle.append(row)
    return triangle
