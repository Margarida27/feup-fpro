# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:38:49 2019

@author: Margarida Viera
"""

def bisect(f, n):
    upper = 1
    lower = 0
    
    while n > 0:
        mid = (lower + upper) / 2
        
        if f(lower) * f(mid) > 0: #if they have the same sign, the product will be positive
            lower = mid
             
        else:
            upper = mid
            
        n -= 1
        
    return round(mid, 5)

print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))

print(bisect(lambda x: x**0.5-0.9, 10))

print(bisect(lambda x: 2*x-20*x**2+1.5, 12))

