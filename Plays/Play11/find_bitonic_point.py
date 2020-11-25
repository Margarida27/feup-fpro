# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:52:19 2019

@author: Margarida Viera
"""

def bitonic_point(f):
    l = f()
    return max(l)   

print(bitonic_point(lambda: [2, 6, 10, 25, 60, 30, 25, 10, 0]))