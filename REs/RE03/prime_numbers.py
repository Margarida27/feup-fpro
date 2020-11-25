# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:41:58 2019

@author: Margarida Viera
"""

num = int(input())
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
if (divisores > 2):
    print('False')
else:
    print('True')      


