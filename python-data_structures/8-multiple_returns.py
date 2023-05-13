#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) is 0:
        return (len(sentence), None)
    for i in sentence:
        return (len(sentence), i)
