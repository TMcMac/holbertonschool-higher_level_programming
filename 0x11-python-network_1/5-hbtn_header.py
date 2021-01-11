#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    if argv[1]:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
