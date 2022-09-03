#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = 1
        for j in i:
            if n == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            n = l + 1
        print()
