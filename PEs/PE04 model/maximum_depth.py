# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:32:34 2019

@author: Margarida Viera
"""

def maximum_depth(l):
    if l == []:
        return 1
    maxi = 0
    for lst in l:
        depth = maximum_depth(lst)
        if depth > maxi:
            maxi = depth
    return maxi + 1

print(maximum_depth( [[[], [], [[]]], [[[[]]]]]))
        
    