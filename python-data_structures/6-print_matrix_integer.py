#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        if not sublist:
            print()
        else:
            for i in sublist:
                if i == sublist[-1]:
                    print("{:d}".format(i))
                else:
                    print("{:d}".format(i), end=" ")
