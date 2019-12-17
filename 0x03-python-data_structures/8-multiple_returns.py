#!/usr/bin/python3
def multiple_returns(sentence):
    Tot = len(sentence)
    MyChar = sentence[0] if Tot > 0 else None
    NewOne = Tot, Mychar
    return(NewOne)
