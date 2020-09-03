#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    args = argv[1:]

    if len(args) is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(args[0])
        b = int(args[2])
        op = str(args[1])
        if op is "+":
            print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op is "-":
            print("{:d} {} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op is "/":
            print("{:d} {} {:d} = {:d}".format(a, op, b, div(a, b)))
        elif op is "*":
            print("{:d} {} {:d} = {:d}".format(a, op, b, mul(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
