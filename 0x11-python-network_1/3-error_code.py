#!/usr/bin/python3
"""
a Python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""

if __name__ == '__main__':
    from liburl import request, error
    from sys import argv

    try:
        with request.urlopen(argv[1]) as response:
            html = response.read()
            content = html.decode("utf-8")
            print(content)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
