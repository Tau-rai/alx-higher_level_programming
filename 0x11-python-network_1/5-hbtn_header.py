#!/usr/bin/python3
"""
This modules has a script that takes a in URL, sends a request to it
and displays the value of the X-Request-Id variable found in  the header
"""

import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    request_id = req.headers.get("X-Request-Id")
    if request_id is not None:
        print(request_id)
