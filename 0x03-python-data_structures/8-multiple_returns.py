#!/usr/bin/python3
def multiple_returns(sentence):
    MyVar = len(sentence)
    if (not sentence):
        return (MyVar, None)
    else:
        return (MyVar, sentence[0])
