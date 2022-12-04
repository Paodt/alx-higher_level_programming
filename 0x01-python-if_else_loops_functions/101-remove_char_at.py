#!/usr/bin/python3

def remove_char_at(str, n):
    rm = ''
    for f in range(len(str)):
        if f != n:
            rm += str[f]
            return rm
