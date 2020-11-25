# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:58:30 2019

@author: Margarida Viera
"""

names = input('names: ')
ages = input('ages: ')
answer = ''
n = len(ages)

for i in range(n):
    answer += str(names[i]) + '-' + str(ages[i]) 
    
print(answer)

