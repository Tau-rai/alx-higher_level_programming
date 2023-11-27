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

    nw_lines = []
    start = 0
    for k, char in enumerate(text):
        if char in delims:
            nw_lines.append(text[start:k+1].strip())
            start = k+1
    nw_lines.append(text[start:].strip())

    nw_lines = [line.strip() for line in nw_lines]

    if nw_lines:
        print("\n\n".join(nw_lines[:-1]), end="\n\n" if nw_lines[:-1] else "")
        print(nw_lines[-1], end="")
