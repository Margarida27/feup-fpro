# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:51:02 2019

@author: Margarida Viera
"""

n = int(input())
for i in range(1, n + 1):
    if (i % 3 == 0 and i % 5 == 0):
        i = i
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i, end =' ')