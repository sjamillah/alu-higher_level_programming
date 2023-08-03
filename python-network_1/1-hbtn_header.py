#!/usr/bin/python3
# script that sends a request to the url and displays the value  of the variable X-Request_Id in the header


import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
