# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:25:53 2019

@author: Margarida Viera
"""

def gcd_rec(n1, n2):
    
    if n2 == 0:
        return n1
    
    else:
        return gcd_rec(min(n1, n2), max(n1, n2) % min(n1, n2))
    
print(gcd_rec(8, 16))

