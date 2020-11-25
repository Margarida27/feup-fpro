# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:24:39 2019

@author: Margarida Viera
"""

def treasure(clues):
    initial = (0,0)
    while initial in clues:
        initial = clues.pop(initial)
    return initial
    
print(treasure({(0,0): (1,0), (1,0): (2,0), (2,0): (3,0)}))
print(treasure({(0,0): (1,0), (2,1): (3,5), (1,0): (2,1)}))
print(treasure({(0,0): (5,6), (7,8): (6,7), (5,6): (6,7), (6,7): (7,8)}))