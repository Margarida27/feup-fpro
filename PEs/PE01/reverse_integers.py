# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:49:48 2019

@author: Margarida Viera
"""

num = int(input('Number: '))

aux = num
count = 0
while aux > 0:
    aux //= 10
    count += 1
    
output = 0   
for i in range(count - 1, -1, -1):
    digit = num % 10
    output += digit * (10 ** i)
    num //= 10
    
print(output)
    