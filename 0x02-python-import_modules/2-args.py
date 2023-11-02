#!/usr/bin/python3
import sys
if __name__ == "__main__":
    nargs = len(sys.argv)
    cmd = nargs - 1

    if nargs == 1:
        print("{:d} arguments.".format(cmd))
    elif nargs == 2:
        print("{:d} argument:\n{:d}: {:s}".format(cmd, cmd, sys.argv[1]))
    else:
        print("{:d} arguments:".format(cmd))
        for k in range(1, nargs):
            print("{:d}: {:s}".format(k, sys.argv[k]))
