# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 14:39:53 2019

@author: Margarida Viera
"""

from functools import reduce 

def map_reduce(n1, n2):
    sqr = [n ** 2 for n in range(n1, n2) if not n % 2 == 0]
        
    return reduce(lambda x,y: x * y if x * y < 50 else x + y, sqr)

print(map_reduce(0, 10))
        
    
    