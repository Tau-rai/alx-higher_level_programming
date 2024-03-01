#!/usr/bin/python3
"""
This module contains a script that takes in a url, send a request and
displays the body of the response
"""


import sys
from urllib import request, error


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read().decode('utf-8')
    except error.HTTPError as e:
        print('Error code: ', e.code)
    except error.URLError as e:
        print('Error code: ', e.reason)
    else:
        print(body)
