#!/usr/bin/python3
"""A simple python script to find peaks in an unsorted array"""


def find_peak(list_of_integers):
    """Fine a peak in an unsorted list"""
    peaks = []
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        return max(list_of_integers)
    """
    if len(list_of_integers) == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    nums = list_of_integers[:]
    high = index(max(nums))
    if high == 0 or high == len(nums) - 1:
        return nums[high]

    h = 0
    i = 1
    j = 2
    if nums[h] >= nums[i]:
        peaks.append(nums[h])

    while i < (len(nums) - 2):
        if nums[h] <= nums[i] >= nums[j]:
    """
