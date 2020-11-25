# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:38:02 2019

@author: Margarida Viera
"""

def collatz(n):
    string = ''
    if n == 1:
        return '1'
    else:
        while n != 1:
           string += str(n) + ','
           if n % 2 == 0:
               n = n / 2
               n = int(n)
           else:
               n = n * 3 + 1
               n = int(n)
        string = string + '1'
        return string

print(collatz(3))
print(collatz(12))
print(collatz(1))
print(collatz(10))


