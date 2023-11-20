#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for k in range(x):
        try:
            my_list[k] = int(my_list[k])
            print("{:d}".format(my_list[k]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            raise
    print()
    return counter
