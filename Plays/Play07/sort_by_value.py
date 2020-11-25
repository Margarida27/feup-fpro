# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:51:38 2019

@author: Margarida Viera
"""

def sort(elem):
    return (elem[1], elem[0])

def sort_by_value(dict1):
    l = dict1.items()
    return sorted(l, key = sort, reverse = False)
    
print(sort_by_value({'Blue': '#0000FF', 'Green': '#008000', 'Black': '#000000', 'White': '#FFFFFF'}))