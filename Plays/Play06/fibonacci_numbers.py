# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:00:01 2019

@author: Margarida Viera
"""

def fib(n):
    if n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append((sequence[i - 2]) + (sequence[i - 1]))
        return sequence

print(fib(7))
        