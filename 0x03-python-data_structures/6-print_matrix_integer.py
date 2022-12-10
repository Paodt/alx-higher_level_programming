#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    length1 = len(matrix)
    for i in range(length1):
        length2 = len(matrix[i])
        for j in range(length2):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
