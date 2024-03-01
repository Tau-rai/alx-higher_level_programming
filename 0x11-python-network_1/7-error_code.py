#!/usr/bin/python3
"""
This module contains a script that takes in a url, send a request and
displays the body of the response
"""


import sys
import requests


if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if req.status_code >= 400:
            print("Error code: ", req.status_code)
    else:
        print(req.text)
