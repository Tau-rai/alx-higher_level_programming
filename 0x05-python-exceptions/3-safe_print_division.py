#!/usr/bin/python3

def safe_print_division(a, b):
    res = None
    try:
        res = a / b
        print("Inside result: {}". format(res))
    except ZeroDivisionError:
        print("Inside result: {}". format(res))
        return None
    finally:
        return res
