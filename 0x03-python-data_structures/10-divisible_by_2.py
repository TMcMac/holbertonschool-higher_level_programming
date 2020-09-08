#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    results = []
    for num in my_list:
        if num % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results
