#!/usr/bin/python3


def print_last_digit(number):
    last_digit = number
    if last_digit < 0:
        last_digit *= -1
    last_digit %= 10
    print(last_digit, end='')
    return (last_digit)
