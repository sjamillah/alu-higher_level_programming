#!/usr/bin/python3
# Script that fetches a URL


import urllib.request

if __name__ == '__main__':
    url = 'https://alu-intranet.hbtn.io/status'
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
