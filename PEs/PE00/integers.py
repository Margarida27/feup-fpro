# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:45:53 2019

@author: Margarida Viera
"""

ints = [1, 2, 2, 3, 5, 9, 13, 21, 34]
num = int(input())
less = 'Less:'
greater = 'Greater:'

for i in ints:
    if i < num:
        less += ' ' + str(i)
    elif i > num:
        greater += ' ' + str(i) 

print(less)
print(greater)