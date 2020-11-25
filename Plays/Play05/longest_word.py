# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:59:20 2019

@author: Margarida Viera
"""

def longest(s):
    s = s.split(' ')
    longest = 0
    for word in s:
        if len(word) > longest:
            longest = len(word)
    return longest

print(longest('A list with some words'))
print(longest('Unnecessarily long sentence since the longest word is the first one'	))
        
        