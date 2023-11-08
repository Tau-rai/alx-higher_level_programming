#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for k in range(len(roman_string)):
        if k > 0 and r_dict[roman_string[k]] > r_dict[roman_string[k - 1]]:
            num += r_dict[roman_string[k]] - 2 * r_dict[roman_string[k - 1]]
        else:
            num += r_dict[roman_string[k]]
    return num
