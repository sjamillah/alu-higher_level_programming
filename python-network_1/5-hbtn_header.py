#!/usr/bin/python3
"""script that takes a url and display the values"""


import requests
import sys


if __name__ == "__main__":
    """display the contents"""
    url = sys.argv[1]
    response = requests.get(url)
    print("{}".format(response.headers.get('X-Request-Id')))
