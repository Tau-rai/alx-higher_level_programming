#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nargs = len(sys.argv) - 1
    result = 0
    if nargs == 0:
        print("{:d}".format(nargs))
    else:
        for num in sys.argv[1:]:
            result += int(num)
        print("{:d}".format(result))
