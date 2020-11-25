# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:02:13 2019

@author: Margarida Viera
"""

n1 = int(input())
n2 = int(input())
if n2 >= 100:
    result = (n1 * 1000) + n2
elif n2 >= 10:
    result = (n1 * 100) + n2 
elif n2 >= 1:
    result = (n1 * 10) + n2
print(result)
