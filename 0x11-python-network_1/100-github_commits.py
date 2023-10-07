#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of the repository
   “rails” by the user “rails”. You must use the GitHub API,
   here is the documentation https://developer.github.com/v3/repos/commits/
   Print all commits by: `<sha>: <author name>` (one by line)
   Takes 2 arguments in order to solve this challenge.
"""
import requests
import sys


if __name__ == "__main__":
    commits_url = "https://api.github.com/" + \
        "repos/{}/{}/commits".format(sys.argv[1], sys.argv[2])
    response = requests.get(commits_url)
    if response.status_code == requests.codes.ok and len(response.text) > 0:
        try:
            obj = response.json()
            for i, j in enumerate(obj):
                if i == 10:
                    break
                if type(j) is dict:
                    name = j.get("commit").get("author").get("name")
                    print("{}: {}".format(j.get("sha"), name))
        except ValueError as invalid_json:
            pass
