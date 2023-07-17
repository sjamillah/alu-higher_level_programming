#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        weight = 0
        score = 0
        for tuple in my_list:
        weight += (tuple[0] * tuple[1])
        score += (tuple[1])
        return weight / score
