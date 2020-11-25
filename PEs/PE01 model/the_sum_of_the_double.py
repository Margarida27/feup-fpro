# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:50:17 2019

@author: Margarida Viera
"""

d = int(input('d:'))
num = int(input('num:'))
aux = num
total = 0

while aux > 0:
    digit = aux % 10
    if digit > d:
        total += digit * 2
    aux //= 10

print(total)
    
    