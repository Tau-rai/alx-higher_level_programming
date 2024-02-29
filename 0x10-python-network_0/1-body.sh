#!/bin/bash
# Takes in a URL, sends a GET request and displays the body

STATUS=$(curl -s -o /dev/null -I -w "%{http_code}" "$1")

if [ "$STATUS" -eq 200 ]
then
    curl -s "$1"
fi