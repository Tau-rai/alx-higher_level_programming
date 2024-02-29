#!/bin/bash
# Takes in a URL and sends GET request and displays body of the response
curl -s -H "X-School-User-Id: 98" "$1"
