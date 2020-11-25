# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:15:48 2019

@author: Margarida Viera
"""

def odd_range(start, stop, step):
    if start % 2 == 0:
        start += 1
        
    while start < stop:
        yield start
        start += 2 * step
        
print(odd_range(100, 150, 5))