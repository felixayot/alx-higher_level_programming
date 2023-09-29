#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
   http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    value = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=value)
    if response.status_code != requests.codes.ok or len(response.text) <= 0:
        print('No result')
        sys.exit()
    else:
        try:
            obj = response.json()
            if len(obj) == 0:
                print('No result')
                sys.exit()
            obj_id = obj.get('id')
            obj_name = obj.get('name')
            print("[{}] {}".format(obj_id, obj_name))
        except ValueError as invalid_json:
            print('Not a valid JSON')
