#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
        num = [tuple[0] * tuple[1] for tuple in my_list]
        den = [tuple[1] for tuple in my_list]
        return (sum(num)/sum(den))
