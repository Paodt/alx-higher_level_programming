#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last = number % 10
        print("{:d}".format(last), end='')
    elif number <= 0:
        last = number % -10
        last = last * -1
        print("{:d}".format(last), end='')
    return last
