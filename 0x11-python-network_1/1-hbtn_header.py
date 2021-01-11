#!/usr/bin/python3
'''a Python script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id'''

from sys import argv
import urllib.request

with urllib.request.urlopen(argv[1]) as response:
    head = response.getheaders()
    for item in head:
        if item[0] == 'X-Request-Id':
            print(item[1])
