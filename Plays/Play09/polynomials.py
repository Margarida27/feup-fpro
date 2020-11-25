# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:22:11 2019

@author: Margarida Viera
"""

def evaluate(a, x):
    return sum([i * (x ** exp) for exp, i in enumerate(a)])

print(evaluate([1, 2, 4], 5))