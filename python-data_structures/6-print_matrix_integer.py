#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        i = 0
        for i in sublist:
            if i == (len(sublist) - 1):
                print("{:d}".format(i))
            else:
                print("{:d}".format(i), end=" ")
            i+=1
            print("")
