#!/usr/bin/python3
for alph in range(122, 96, -1):
    if alph % 2 == 0:
        print("{:c}".format(alph), end='')
    else:
        uppr = alph - 32
        print("{:c}".format(uppr), end='')
