# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:40:12 2019

@author: Margarida Viera
"""

def get_composites(n):
    composites = []
    
    primes = [x for x in range(n + 1) if all(x % y != 0 for y in range(2, x))]
    
    for j in range(4, n + 1):
        if j not in primes:
            yield j
            composites.append(j)

print(get_composites(10))
  