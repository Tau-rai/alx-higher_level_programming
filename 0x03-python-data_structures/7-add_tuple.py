#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    result = tuple(map(lambda x, y: x + y, tuple_a[:2], tuple_b[:2]))
    return result
