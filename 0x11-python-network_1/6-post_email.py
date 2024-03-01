#!/usr/bin/python3
"""
This module has a script that takes in a URL and an email, sends a POST request
and displays the body of the response
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    print(req.text)
