# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:34:54 2019

@author: Margarida Viera
"""

def f(x):
    if x >= 5:
        return 5 - x
    else:
        return x
    
def sort_by_f(alist):
    return sorted(alist, key = lambda x: f(x), reverse = False)

print(sort_by_f([-10, -6, 2, 5, 90]))
