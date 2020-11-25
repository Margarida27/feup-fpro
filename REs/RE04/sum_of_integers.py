# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:58:06 2019

@author: Margarida Viera
"""

def sum_numbers(n):   
    sum_numbers = 0
    for i in range(n + 1):
        sum_numbers = sum_numbers + i
    return sum_numbers
       
n = int(input())
print(sum_numbers(n))








