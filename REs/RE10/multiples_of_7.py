# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:08:14 2019

@author: Margarida Viera
"""

def multiples_of7(n):
    multiples = []
    for x in range(0, n):
        if x % 7 == 0:
            yield x
            multiples.append(x)
            

def multiples_of7(n):      
    return (i for i in range(n) if i % 7 == 0)     


