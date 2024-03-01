#!/usr/bin/python3
"""
This module contains a script that takes in a url, send a request and
displays the body of the response
"""


import sys
from urllib import request, error


def request_sent(url):
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == "__main__":
    request_sent(sys.argv[1])
