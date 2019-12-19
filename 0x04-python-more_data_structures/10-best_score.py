#!/usr/bin/python3
def best_score(a_dictionary):
    MaxValue = 0
    MaxKey = None
    if not a_dictionary:
        return (None)
    for Key, Value in a_dictionary.items():
        if Value > MaxValue:
            MaxValue = Value
            MaxKey = Key
    return MaxKey
