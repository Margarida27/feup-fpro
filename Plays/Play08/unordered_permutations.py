# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:02:33 2019

@author: Margarida Viera
"""

def permutations(atuple):
    # BASE CASE
    if len(atuple) == 1:
        return {atuple}
    
    if len(atuple) == 2:
        return {atuple}.union({atuple[::-1]})
        
    # RECURSIVE CASE
    permuts = set() # final set with all possible permutations
    
    for elem in atuple:
        remain = [x for x in atuple if x != elem]
        remain = tuple(remain)
        sub_permut = permutations(remain) # sub permutations
        
        for sub_elem in sub_permut:
            permuts.add(tuple([elem] + list(sub_elem)))
        
    return permuts

print(permutations(('A', 'B', 'C')))
