# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 16:32:26 2019

@author: Margarida Viera
"""

def rearrange(l):
    if l == []:
        return []
    else:
        return [n for n in l if n <= 0] + [n for n in l if n > 0]
   
print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))