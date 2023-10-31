#!/usr/bin/python3

def uppercase(str):
    res = ""
    for lower in str:
        if ord(lower) >= 97 and ord(lower) < 123:
            upper = chr(ord(lower) - 32)
        else:
            upper = lower
        res += upper

    print("{}".format(res))
