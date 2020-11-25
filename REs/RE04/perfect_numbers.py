# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:22:59 2019

@author: Margarida Viera
"""

def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    is_perfect = (sum == n)
    return is_perfect

n = int(input())
print(is_perfect(n))

