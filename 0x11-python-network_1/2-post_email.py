#!/usr/bin/python3
""" 
a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""

if __name__  == '__main__':
    from sys import argv
    from  urllib import request, parse
    if argv[2]:
        url = argv[1]
        value = {}
        value['email'] = argv[2]
        data = parse.urlencode(value).encode('UTF-8')
        req = request.Request(url, data)
        with request.urlopen(req) as response:
            content = response.read()
            print(content.decode("UTF-8"))
