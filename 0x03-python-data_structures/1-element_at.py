#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    id = my_list[idx]
    if idx < 0:
        return (None)
    if idx > length - 1:
        return (None)
    return (id)
