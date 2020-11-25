# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:56:32 2019

@author: Margarida Viera
"""

n = int(input())
n = str(n)
count = 0

for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        count += 1

print(count)

    
    