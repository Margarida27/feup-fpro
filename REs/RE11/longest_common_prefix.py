# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:49:11 2019

@author: Margarida Viera
"""


def prefix(w1, w2):
    for i in range(1, len(w1) + 1):
        if w1[:i] == w2[:i]:
            continue
        else:
            return w1[:i - 1]
    return w1
        
def longest_prefix(words):
    
    #Base case
    if len(words) == 1:
        return words[0]
    
    #Recursive case
    prefixes = []
    
    for i in range(len(words) - 1):
        pre = prefix(words[i], words[i + 1])
        prefixes.append(pre)
        
    x = longest_prefix(prefixes)    
    return x

print(longest_prefix(['apple', 'apply', 'ape', 'april']))
    
    
    