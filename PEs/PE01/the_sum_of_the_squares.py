# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:53:03 2019

@author: Margarida Viera
"""

d = int(input('Digit[d]: '))
num = int(input('Number: '))
total = 0

while num > 0:
    digit = num % 10
    if digit > d:
        total += digit ** 2
    num //= 10
    
print(total)