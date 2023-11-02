#!/usr/bin/python3
import re

if __name__ == "__main__":
    with open("hidden_4.py", "r") as src_file:
        src_file = src_file.read()

    matches = re.findall(r'\b[^_][^_]*_[^_]+\b', src_file)
    
    for word in matches:
        print(word)    
