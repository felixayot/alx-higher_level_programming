#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of
   the X-Request-Id variable found in the header of the response.
"""
from urllib import request
import sys


if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as response:
        page = response.info()
        for header in page._headers:
            if header[0] == "X-Request-Id":
                print(header[1])
