#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = 0
n = number

if number < 0:
    d = number % -10

elif number > 0:
    d = number % 10

if d == 0:
    print("Last digit of {} is {} and is 0".format(number, d))

elif d > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, d))

elif d < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(n, d))
