# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:48:04 2019

@author: Margarida Viera
"""

# SOLUTION USING ITERTOOLS
#from itertools import product
#
#def combos(alist):
#    combos = list(product(*([alist] * 3)))
#    return [''.join(elem) for elem in combos]

def brute_force(f, l):
    combinations = list(str(x)+str(y)+str(z) for x in l for y in l for z in l)
    return list(filter(f, combinations))

print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))
print()
print(brute_force(lambda x: x[0] == 'c' and x not in ('cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))
print()
print(brute_force(lambda x: abs(int(x)) == 1 if x.isdigit() else False, ['-', '0', '1', '2']))
print()
print(brute_force(lambda x: int(x) ** 2 < 5, ['0', '1', '2', '3', '4']))
