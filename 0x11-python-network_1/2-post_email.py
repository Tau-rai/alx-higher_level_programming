#!/usr/bin/python3
"""
This module has a script that takes in a URL and an email, sends a POST request
and displays the body of the response (decoded in utf-8)
"""


from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
