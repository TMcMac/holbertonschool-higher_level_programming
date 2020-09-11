#!/usr/bin/python3
def weight_average(my_list=[]):
    grade = 0
    weight = 0
    if my_list:
        for i in my_list:
            grade += (i[0] * i[1])
            weight += i[1]
        grade /= weight
    return grade
