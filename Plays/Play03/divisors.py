# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:04:23 2019

@author: Margarida Viera
"""

num = int(input())
sum = 0
for i in range(1, num + 1):
	if (num % i == 0):
		sum += i
print(sum) 
