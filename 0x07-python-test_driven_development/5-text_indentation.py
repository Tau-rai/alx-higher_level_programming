#!/usr/bin/python3
"""
A function that print a text with 2 new lines after a specific delimiter

Args:
    text (str): a string of characters
"""


def text_indentation(text):
    """
    A function that splits a setence on . or ? or :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delims = [".", "?", ":"]

    new_lines = []
    start = 0
    for k, char in enumerate(text):
        if char in delims:
            new_lines.append(text[start:k+1].strip())
            start = k+1
    new_lines.append(text[start:].strip())
    #remove white spaces from each line
    new_lines = [line.strip() for line in new_lines]

    if new_lines:
        print("\n\n".join(new_lines[:-1]), end="\n\n" if new_lines[:-1] else "")
        print(new_lines[-1], end="")
