# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:59:22 2019

@author: Margarida Viera
"""

n = float(input())
a = 0
b = n 
mid = (a + b) / 2
while not(round(a, 5) == round(b, 5) or mid * mid == n):
    if mid * mid < n:
        a = mid
    else:
        b = mid
    mid = (b + a) / 2
print(round(mid, 5))