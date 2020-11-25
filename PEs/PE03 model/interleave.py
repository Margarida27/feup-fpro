# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:54:16 2019

@author: Margarida Viera
"""

# RECURSIVE SOLUTION
def interleave(l1, l2):
    # BASE CASE
    if type(l1) != list:
        return [l1, l2]
    
    if len(l1) == 0 or len(l2) == 0:
        return []
    
    # RECURSIVE CASE
    return interleave(l1[0], l2[0]) + interleave(l1[1:], l2[1:])

# RECURSIVE SOLUTION USING FOR 
def interleave(l1, l2):
    # BASE CASE
    if type(l1) != list:
        return [l1, l2]
    
    inter = []
    for x, y in zip(l1, l2):
        inter += interleave(x, y)
        
    return inter 

print(interleave([1, [4,2]], [3, [7,4]]))
print()
print(interleave(['a','b','c'], [1,2,3,4,5]))
print()
print(interleave([], [1,2]))