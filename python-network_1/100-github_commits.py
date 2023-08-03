#!/usr/bin/python3
'''Uses github api to print last ten commits to given repo by given user'''
import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    username = sys.argv[2]
    headers = {'accept': 'application/vnd.github+json'}
    data = {'per_page': 10, 'page': 1}
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    response = requests.get(url, headers=headers, params=data)
    json_data = response.json()
    for entry in json_data:
        print(f"{entry.get('sha')}: \
{entry.get('commit').get('author').get('name')}")
