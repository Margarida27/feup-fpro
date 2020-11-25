# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:48:04 2019

@author: Margarida Viera
"""

def paint(n, boards):
    l = []

    if n == 1:
        return max(boards)
    
    else:
        for elem, time in enumerate(boards):
            if (len(boards[0:elem]) > 0) and (len(boards[0:elem]) + n - 2 < len(boards)):
                l.append((paint(n - 1, boards[elem:])) + max(boards[0:elem]))
        
        return min(l)
    
def paint(n, boards):
    if n==1: return max(boards)
    ls = []
    for i in range(len(boards)-n+1):
        ls.append(paint(1, boards[:i+1])+paint(n-1, boards[i+1:]))
    return min(ls)

def paint(n, boards):
    if n == 1:
        return max(boards)
    return min(max(boards[:i]) + paint(n-1, boards[i:]) for i in range(1, len(boards)-n+2))
