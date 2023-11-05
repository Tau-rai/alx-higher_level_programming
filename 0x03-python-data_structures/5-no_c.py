#!/usr/bin/python3

def no_c(my_string):
    new_list = [c.strip('Cc') for c in my_string]
    new_string = ''.join(str(k) for k in new_list)

    return new_string
