#!/usr/bin/python3
import sys
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    if len(sys.argv) != 4:
        usage = "Usage: ./100-my_calculator.py <a> <operator> <b>"
        print("{}".format(usage))
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        op = "Unknown operator. Available operators: +, -, * and /"
        print("{:s}".format(op))
        sys.exit(1)
