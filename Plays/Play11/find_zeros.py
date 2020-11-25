# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:00:35 2019

@author: Margarida Viera
"""

def count_zeros(f):
    l = f()
    size = len(l)
    ub = size
    mid = ub // 2
    lb = 0
    while l[mid] == l[mid + 1]:
        if l[mid] == 1:
            lb = mid
            mid = (ub + lb) // 2
        else:
            ub = mid
            mid = (ub + lb) // 2
    return size - mid -1

print(count_zeros(lambda: [1, 1, 1, 0, 0]))
print()
print(count_zeros(lambda: [1]*80000000 + [0]*70000000))
