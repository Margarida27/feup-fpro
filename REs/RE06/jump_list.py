# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:39:39 2019

@author: Margarida Viera
"""

def jump(l):
    if l == [-1]:
        return 0
    else:
        ix = 0
        jumps = 0
        while l[ix] != -1:
            ix = l[ix]
            jumps += 1
        return jumps
    
print(jump([5, 7, 6, 3, 2, -1, 4, 1]))
print(jump([8, 11, 6, 2, 7, 1, 4, -1, 10, -1, 3, 9]))
print(jump([5, 11, 6, 2, 7, 1, 4, -1, 10, -1, 3, 9]))
	
            
        