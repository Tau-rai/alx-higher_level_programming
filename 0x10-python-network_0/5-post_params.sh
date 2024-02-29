#!/bin/bash
# Takes ina URL, send a POST request and diplays body of the response
curl -s --data-urlencode"email=test@gmail.com&subject=I will always be here for PLD" "$1"
