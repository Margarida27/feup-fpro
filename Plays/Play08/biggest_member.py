# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:12:10 2019

@author: Margarida Viera
"""

def biggest_member(atuple):
    a = ()
    for elem in atuple:
        if type(elem) == tuple:
            if len(elem) > len(a):
                a = elem
            b = biggest_member(elem)
            if len(b) > len(a):
                a = b
    return a
    

print(biggest_member((5, (2, 3, 1))))            
print(biggest_member(('abc', 'jkl', ('abc', 'z', 'def', ('123', 'jkl'))))) 
