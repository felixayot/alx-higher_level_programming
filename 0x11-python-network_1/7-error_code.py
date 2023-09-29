#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
   and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
