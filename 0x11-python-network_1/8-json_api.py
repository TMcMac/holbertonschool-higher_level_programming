#!/usr/bin/python3
"""
a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    data = {}
    if len(argv) >= 2:
        data['q'] = argv[1]
    else:
        data['q'] = ""
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json_string = response.json()
        if json_string == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_string['id'], json_string['name']))
    except Exception as err:
        print("Not a valid JSON")
