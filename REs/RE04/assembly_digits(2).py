# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:48:22 2019

@author: Margarida Viera
"""

def adigits(a, b, c):
    n1 = int(a + b + c)
    n2 = int(a + c + b)
    n3 = int(b + a + c)
    n4 = int(b + c + a)
    n5 = int(c + a + b)
    n6 = int(c + b + a)
    adigits = max(n1, n2, n3, n4, n5, n6)    
    return adigits