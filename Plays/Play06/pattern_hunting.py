# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:07:45 2019

@author: Margarida Viera
"""

def pattern_hunting(l1, l2, p):
    patterns = []
    for string in l1:
        if p in string:
            ix = l1.index(string)
            patterns.append(l2[ix])
    for string in l2:
        if p in string:
            ix = l2.index(string)
            patterns.append(l1[ix])
    return sorted(patterns, reverse = True)

print(pattern_hunting(['not found', 'pattern here', 'skip', 'next... or not?'], ['pattern here indeed', 'i want to be chosen', 'not my day', 'sneakypatternbutitisthere'], 'pattern'))