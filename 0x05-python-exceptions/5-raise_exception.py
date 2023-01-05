#!/usr/bin/python3
def raise_exception():
    num = 1
    if not type(num) is str:
        raise TypeError()
