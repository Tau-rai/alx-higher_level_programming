#!/bin/bash
# Takes in a URL and displays the size of the body of the response

# curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
if [ $# -ne 1 ]
then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | awk '/Content-Length/ {print $2}'
