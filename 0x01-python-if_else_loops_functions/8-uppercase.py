#!/usr/bin/python3
def uppercase(str):
    c = 0

    for i in range(len(str)):
        c = ord(str[i])

        if c > 96 and c < 123:
            c = c - 32

        print("{}".format(chr(c)), end="")

    print()
