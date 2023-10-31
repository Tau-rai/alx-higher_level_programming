#!/usr/bin/python3

for num in range(90, 64, -1):
    print("{0}{1}".format(chr(num + 32), chr(num)), end="")
