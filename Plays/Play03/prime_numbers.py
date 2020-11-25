# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 10:58:35 2019

@author: Margarida Viera
"""

lower = int(input())
upper = int(input())
count = 0
res = 'Prime numbers between ' + str(lower) + ' and ' + str(upper) + ' are:'
if upper > lower:
    for i in range(lower, upper + 1):
        for u in range(1, i + 1):
            if i % u == 0:
                count += 1
        if count == 2:
            res = res + ' ' + str(i)
        count = 0
print(res)
