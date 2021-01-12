#!/usr/bin/python3
"""
a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    data = {}
    if argv[1]:
        data[q] = argv[1]
    else:
        data[q] = ""
    r = requests.post(url, data=data)
    try:
        json_s = r.json()
        if json_s == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_s['id'], json_s['name']))
    except Exception as err:
        print("Not a valid JSON")
