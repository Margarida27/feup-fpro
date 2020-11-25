# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:54:39 2019

@author: Margarida Viera
"""

quat = int(input('Quaternary number: '))

aux = quat
count = 0
while aux > 0:
    aux //= 10
    count += 1

dec = 0    
for i in range(0, count):
     digit = quat % 10
     dec += digit * (4 ** i)
     quat //= 10

print(dec)