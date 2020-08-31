#!/usr/bin/python3


i = 1

while (i < 89):
    if (i % 10 == 0):
        i += int(i / 10) + 1
    else:
        print("{:02d},".format(i), end=' ')
        i += 1
print(89)
