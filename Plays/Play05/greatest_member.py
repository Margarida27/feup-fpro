# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:50:56 2019

@author: Margarida Viera
"""
def score(atuple):
    score = 0
    for tup in atuple:
        if type(tup) == str:
            tup = list(tup)
            for x in tup:
                score += ord(x)
        elif type(tup) == tuple:
            tup = list(tup)
            for subtup in tup:
                if type(subtup) == str:
                    subtup = list(subtup)
                    for y in subtup:
                        score += ord(y)
                elif type(subtup) == tuple:
                    subtup = list(subtup)
                    for elem in subtup:
                        elem = list(elem)
                        for z in elem:
                            score += ord(z)
    return score

def sort(atuple):
    sorted_tuple = sorted(atuple, key = score, reverse = True)
    return sorted_tuple

def greatest_member(atuple):
    if atuple == ():
        return ()
    else:
        output = sort(atuple)[0]
        return output
    

    
