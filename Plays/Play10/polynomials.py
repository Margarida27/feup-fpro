# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:32:11 2019

@author: Margarida Viera
"""

def evaluate(a, x):
    l = [x ** exp for exp in range(len(a))]
    return [i * j for i in a for j in l]

print(evaluate([1, 2, 4], 5))

