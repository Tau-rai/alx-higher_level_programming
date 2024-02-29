#!/bin/bash
# Takes ina URL, send a POST request and diplays body of the response
curl -s -X POST --data-urlencode "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
