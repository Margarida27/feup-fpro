# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:57:33 2019

@author: Margarida Viera
"""

def permuta(alist,step=0):
    l = [] # list with all possible permutations
    
    # BASE CASE
    if len(alist) == 0:
        return []
    
    # RECURSIVE CASE        
    for count in range(step, len(alist)):
        lst = alist[:]    
        v = lst[step]
        lst[step] = lst[count]
        lst[count] = v  
        l.append(lst)
        step += 1
        for elem in permuta(lst, step):
            if elem not in l:
                l.append(elem)
        step -= 1
            
    return l

print(permuta(['A', 'B', 'C']))
print()
print(permuta(['Joe', 'Mary', 'John']))

