# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:08:57 2019

@author: Margarida Viera
"""

def nth_lowest(lnum, n):
    l = sorted(lnum, reverse = False)
    return l[n -1]

print(nth_lowest([73, 100, 23, 18, 84, 61, 56, 75, 92, 38, 54, 73, 3, 13], 12))