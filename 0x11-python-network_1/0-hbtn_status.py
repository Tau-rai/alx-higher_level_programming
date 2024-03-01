#!/usr/bin/python3
"""
This module contains a python script that fetches a url
"""


import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        body = response.read()
        f_strng = "\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
            type(body), body, body.decode('utf-8')
        )
        print("Body response:")
        print(f_strng)
