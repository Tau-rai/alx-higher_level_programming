#!/usr/bin/python3
"""
This module has a script that takes in a letter and sends a POST
request to a URL with the letter as a parameter
"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    req = requests.post(url, data={'q': value})

    try:
        data = req.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
