#!/bin/bash
# Takes in a URL, sends a GET request and displays the body

# RESPONSE=$(curl -sI "$1")

# if echo "$RESPONSE" | grep -q "200 OK"
# then
#     curl -s "$1"
# fi
curl -s -X GET "$1"
