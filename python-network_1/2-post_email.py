#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    """"Documented"""
    url = sys.argv[1]
    message = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(message)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))