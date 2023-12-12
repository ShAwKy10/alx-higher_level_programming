#!/usr/bin/python3
def print_last_digit(number):
    ld = 0

    if number > 0:
        ld = number % 10
    elif number < 0:
        ld = number % -10

    print("{}".format(ld))

    return (ld)
