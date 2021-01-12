#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    stat = r.status_code
    if stat >= 400:
        print("Error code: {}".format(stat))
    else:
        print(r.text)
