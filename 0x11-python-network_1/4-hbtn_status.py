#!/usr/bin/python3
"""
This module contains a python script that fetches a url using requests
"""


import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')

    f_string = "\t- type: {}\n\t- content: {}".format(type(req.text), req.text)
    print("Body response:")
    print(f_string)
