#!/usr/bin/python3
'''a Python script that fetches https://intranet.hbtn.io/status'''
import urllib.request
with urllib.request.urlopen('http://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(html), html, html.decode('utf-8')))
