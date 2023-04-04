#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lastd = number % -10
        print(-(lastd), end="")
    else:
        lastd = number % 10
        print((lastd), end="")
    return abs(lastd)
