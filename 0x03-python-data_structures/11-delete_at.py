#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or idx < 0 or idx > len(my_list) - 1:
        pass
    elif idx == 0:
        my_list = my_list[1:]
    elif idx == len(my_list) -1:
        my_list = my_list[:idx]
    else:
        my_list = my_list[:idx] + my_list[(idx + 1):]

    return my_list