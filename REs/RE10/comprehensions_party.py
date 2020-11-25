# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:39:12 2019

@author: Margarida Viera
"""

from math import sqrt

def comprehensions(i, j):
    nums = [n for n in range(i, j + 1) if (str(n)[-1] == '3' or str(n)[-1] == '8')]
    root = tuple([round(sqrt(n), 2) for n in range(i, j + 1)])
    asc = {n: chr(n) for n in range(i, j + 1)}
    return (nums, root, asc)

print(comprehensions(48, 57))