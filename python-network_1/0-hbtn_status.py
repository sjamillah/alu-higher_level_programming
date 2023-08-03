#!/usr/bin/python3
"""Script that fetches a URL"""


import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        data = response.read()
        result = f"Body response:\n\t- type: {type(data)}\n\t- content: {data}\n\t- utf8 content: {data.decode("utf-8")}"
