#!/usr/bin/python3
"""
This modules has a script that takes a in URL, sends a request to it
and displays the value of the X-Request-Id variable found in  the header
"""

import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        request_id = response.getheader("X-Request-Id")
        if request_id is not None:
            print(request_id)
