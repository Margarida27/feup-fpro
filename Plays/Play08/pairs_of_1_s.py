# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:30:08 2019

@author: Margarida Viera
"""

def check(x):
    if type(x) != int:
        x = x[2:]
    if '11' not in x:
        return True
    else:
        return False
    
def no_consecutives1(k):
    bins = [bin(x) for x in range(2 ** k)]
    no_cons = list(filter(lambda x: check(x), bins))
    return len(no_cons)

print(no_consecutives1(7))