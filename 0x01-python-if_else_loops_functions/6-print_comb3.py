#!/usr/bin/python3
for numb in range(1, 90):
    if numb % 10 > numb / 10:
        if numb != 89:
            print("{:02d}".format(numb), end=(", "))
        else:
            print("{:02d}".format(numb))
