# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:40:26 2019

@author: Margarida Viera
"""

def treasure(clues):
    pos = (0,0)
    while pos in clues:
        pos = clues.pop(pos)
    return pos

def treasure(clues):
    pos = (0,0)
    while pos in clues:
        old_pos, pos = pos, clues[pos]
        del clues[old_pos]
    return pos

print(treasure({(0, 0): (5, 6), (7, 8): (6, 7), (5, 6): (6, 7), (6, 7): (7, 8)}))
            
        