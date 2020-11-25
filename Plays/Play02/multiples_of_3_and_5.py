# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:21:46 2019

@author: Margarida Viera
"""

def sum_multiples(n):
    sum = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i     
    return sum