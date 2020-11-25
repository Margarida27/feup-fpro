# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:26:48 2019

@author: Margarida Viera
"""

l1 = int(input())
l2 = int(input())
l3 = int(input())
if (l1 > l2 and l1 > l3) and (l1 > l2 + l3):
    print('Not a triangle')
elif (l2 > l1 and l2 > l3) and (l2 > l1 + l3):
    print('Not a triangle')
elif (l3 > l1 and l3 > l2) and (l3 > l1 + l2):
    print('Not a triangle')
elif (l1 == l2 and l2 == l3):
    print('Equilateral')
elif (l1 != l2 and l2 != l3):
    print('Scalene')
else:
    print('Scalene')
    