#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) is not 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = str(argv[2])
        if op is '+':
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op is '-':
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op is '/':
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
        elif op is '*':
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and / ")
            exit(1)
