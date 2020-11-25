# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:38:32 2019

@author: Margarida Viera
"""

def days_until_empty(C, l):
    i = 0
    full = C
    while C > 0:
        C += l
        while C > full:
            C -= 1  
        i += 1
        C -= i
    return i

print(days_until_empty(10, 0))