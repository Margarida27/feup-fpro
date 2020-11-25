# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:26:51 2019

@author: Margarida Viera
"""

dec = int(input('decimal number: '))
octal = ''

while dec > 0:
    octal += str(dec % 8)
    dec //= 8

final_octal = ''
for i in range(len(octal) - 1, -1, -1):
    final_octal += octal[i]
    
print(final_octal)
