#!/usr/bin/python3
import sys

if __name__=="__main__":
    sum_all = 0
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            sum_all += int(sys.argv[i])
    print(sum_all)
