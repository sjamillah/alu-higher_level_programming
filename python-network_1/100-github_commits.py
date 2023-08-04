#!/usr/bin/python3
"""Uses github api to print last ten commits to given repo by given user"""

from requests import get, auth
import sys

if __name__ == "__main__":
    try:
       repo = sys.argv[1]
       username = sys.argv[2]
       url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
       response = get(url)
       json_data = response.json()
       for entry in (0, 10):
           print(f"{json_data[entry].get('sha')}:, {json_data[entry].get('commit').get('author').get('name')}")
    except:
        pass
