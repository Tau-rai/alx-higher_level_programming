#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    b_key = None
    b_score = None
    for key, score in a_dictionary.items():
        if b_score is None or score > b_score:
            b_key = key
            b_score = score
    return b_key
