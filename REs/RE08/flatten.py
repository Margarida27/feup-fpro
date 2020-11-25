# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:38:21 2019

@author: Margarida Viera
"""

def flatten(alist):
    output = []
    for elem in alist:
        if type(elem) is list:
            output += flatten(elem)
        else:
            output.append(elem)
    return output
    
            
print(flatten(['Hello', [2, [[], False]], [True]]))