#!/usr/bin/python3
"""script that displays the value of var X-Request_Id with url request"""


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
