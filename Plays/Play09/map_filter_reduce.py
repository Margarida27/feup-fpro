# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:07:31 2019

@author: Margarida Viera
"""

from functools import reduce

def map_filter_reduce(lst, f1, f2, f3):
    lst1 = list(filter(f1, lst))
    lst2 = list(map(f2, lst1))
    lst3 = reduce(f3, lst2)
    return lst3

print(map_filter_reduce([1, 2, 3, 4, 5, 6, 7, 8], lambda i: i % 2 == 0, lambda i: i**2, lambda a, b: a+b))