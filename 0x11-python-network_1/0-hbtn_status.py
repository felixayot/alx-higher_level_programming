#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        page = response.read()
        print("Body response:")
        print("\t- type: ", type(page))
        print("\t- content: ", page)
        print("\t- utf8 content: ", page.decode("UTF-8"))
