#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        sign = "-"
    else:
        sign = ""
    l_digit = sign + str(abs(number))[-1]

    return l_digit
