# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:54:37 2019

@author: Margarida Viera
"""

n = int(input())
if n >= 0 and n <= 9:
    n1 = int(str(n))
    n2 = int(str(n) + str(n))
    n3 = int(str(n) + str(n) + str(n))
    final = n1 + n2 + n3
    print (final)   
