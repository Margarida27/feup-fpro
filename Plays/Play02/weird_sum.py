# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:42:24 2019

@author: Margarida Viera
"""

a = int(input())
b = int(input())
par = ((abs(a - b)) % 2 == 0)
impar = ((abs(a - b)) % 2 == 1)
weird_sum = (a + b) + par * (a + b) + impar * (a * b)
print(weird_sum)