#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
        numerator = [tuple[0] * tuple[1] for tuple in my_list]
        denominator = [tuple[1] for tuple in my_list]
        return (sum(numerator) / sum(denominator))
