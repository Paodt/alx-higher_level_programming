#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        for in range(1, len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
        return max
