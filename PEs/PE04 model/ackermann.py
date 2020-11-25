# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:12:32 2019

@author: Margarida Viera
"""

def ackermann(m, n):
    if m == 0:
        return n + 1
    if m != 0 and n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(3, 4))