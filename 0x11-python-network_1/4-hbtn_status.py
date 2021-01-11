#!/usr/bin/python3
"""a Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == '__main__':
    import requests

    response = requests.get('https://intranet.hbtn.io/status')
    content = response.text
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(content), content))
