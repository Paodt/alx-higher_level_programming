#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checker = []
    for i in range(len(my_list)):
        num = my_list[i]
        if num % 2 == 0:
            checker.append(True)
        else:
            checker.append(False)
    return checker
