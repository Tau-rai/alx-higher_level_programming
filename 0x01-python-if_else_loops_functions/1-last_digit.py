#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = "-"
else:
    sign = ""
l_dgt = sign + (str(abs(number)))[-1]

if (int(l_dgt) > 5):
    print(f"Last digit of {number:d} is {l_dgt} and is greater than 5")
elif (int(l_dgt) == 0):
    print(f"Last digit of {number:d} is {l_dgt} and is 0")
else:
    print(f"Last digit of {number:d} is {l_dgt} and is less than 6 and not 0")
