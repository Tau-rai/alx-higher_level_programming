#!/usr/bin/python3
"""
This module contains one function that
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None
    first = 0
    last = len(list_of_integers) - 1

    while first < last:
        mid = (first + last) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            first = mid + 1
        else:
            last = mid
    return list_of_integers[first]
