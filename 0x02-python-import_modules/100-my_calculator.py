#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as math
    from sys import argv

    ops = ['+', '-', '*', '/']

    if __name__ == "__main__":
        if len(argv) is not 4:
            print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
            exit(1)
        elif argv[2] not in ops:
            print("Unknown operator. Available operators: +, -, * and / ")
            exit(1)
        else:
            a = int(argv[1])
            b = int(argv[3])
            op = argv[2]
            if argv[2] is '+':
                print("{} {} {} = {}".format(a, op, b, math.add(a, b)))
            elif argv[2] is '-':
                print("{} {} {} = {}".format(a, op, b, math.sub(a, b)))
            elif argv[2] is '*':
                print("{} {} {} = {}".format(a, op, b, math.mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, op, b, math.div(a, b)))
