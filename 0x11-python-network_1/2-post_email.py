#!/usr/bin/python3
""" 
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__  == '__main__':
    from sys import argv
    from  urllib import request, parse
    value = {'email': argv[2]}
    data1 = parse.urlencode(value)
    data = data1.encode("utf-8")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        content = response.read()
        print(content.decode("UTF-8"))
