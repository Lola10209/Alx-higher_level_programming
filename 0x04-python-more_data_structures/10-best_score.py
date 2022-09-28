#!/bin/usr/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    _max = max(a_dictionary.values())
    for key in a_dictionary:
        if _max == a_dictionary[key]:
            return key
