#!/usr/bin/python3

import sys
if __name__ == "__main__":
    n = len(sys.argv)
    if n == 1:
        print("{:d}".format(n - 1))
    sum = 0
    for i in range(1, n):
        sum = sum + int(sys.argv[i])
    print(sum)
