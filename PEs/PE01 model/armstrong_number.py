# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:42:06 2019

@author: Margarida Viera
"""

num = int(input())
total = 0
aux = num
for i in range(3):
    digit = aux % 10
    total += digit**3
    aux //= 10
print(total == num)
