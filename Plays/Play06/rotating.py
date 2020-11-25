# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:12:20 2019

@author: Margarida Viera
"""

def  rotate_list(l):
    return l[3:] + l[:3]

print(rotate_list([1, 2, 3, 4, 5, 6, 7, 8]))