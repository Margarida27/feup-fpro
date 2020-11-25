# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:44:58 2019

@author: Margarida Viera
"""

from math import floor

def juggler(n, p):
    if p == 0:
        return n
    
    elif juggler(n, p - 1) % 2 == 0:
        return floor(juggler(n, p - 1) ** (1 / 2))
    
    elif juggler(n, p - 1) % 2 == 1:
        return floor(juggler(n, p - 1) ** (3 / 2))

print(juggler(37, 2))
    