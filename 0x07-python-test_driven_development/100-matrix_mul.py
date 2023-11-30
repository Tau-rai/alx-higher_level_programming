#!/usr/bin/python3
"""Module that has a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices lists of integers
        If the list is empty, the function returns None
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")
    if not len(set(len(i) for i in m_a)) <= 1:
        raise TypeError("each row of m_a must be of the same size")
    if not len(set(len(i) for i in m_b)) <= 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for m_a_row in m_a:
        row_result = []
        for m_b_col in zip(*m_b):
            element_sum = sum(x * y for x, y in zip(m_a_row, m_b_col))
            row_result.append(element_sum)
        result.append(row_result)
    return result
