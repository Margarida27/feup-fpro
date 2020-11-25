# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:57:13 2019

@author: Margarida Viera
"""

def sum_digits_rec(n):
    if n < 10:
        return n
    
    else:
        return n % 10 + sum_digits_rec(n // 10) 
    
print(sum_digits_rec(45))