#!/usr/bin/python3
def print_last_digit(number):
    ld = 0
    number = abs(number)

    if number != 0:
        ld = number % 10

    print("{}".format(ld), end="")

    return (ld)
