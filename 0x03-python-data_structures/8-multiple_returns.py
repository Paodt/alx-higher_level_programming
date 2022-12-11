#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "":
        # ch is the first character
        ch = sentence[0]
    else:
        ch = None
    return (len(sentence), ch)
