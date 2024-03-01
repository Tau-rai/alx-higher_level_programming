#!/usr/bin/python3
"""
This module has a script that takes your Github credentials and
uses the Github API to display my id
"""


import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get(url, auth=(username, password))
    data = req.json()
    print(data.get('id'))
