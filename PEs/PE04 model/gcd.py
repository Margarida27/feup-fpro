# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:04:09 2019

@author: Margarida Viera
"""

# Euclid's algorithm says that gcd(a,b) == gcd(b, a(mod b))
# solution using while 
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# solution using recursion
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
print(gcd(25,5))