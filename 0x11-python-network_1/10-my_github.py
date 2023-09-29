#!/usr/bin/python3
"""Takes your GitHub credentials (username and password=PAT) and uses
   the GitHub API to display your id.
"""
import requests
import sys


if __name__ == "__main__":
    user_url = "https://api.github.com/" + "user"
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(user_url,
                            auth=requests.auth.HTTPBasicAuth(username,
                                                             password))
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            obj = response.json()
            print(obj.get('id'))
        except ValueError as invalid_json:
            print('Not a valid JSON')
    else:
        print(None)
