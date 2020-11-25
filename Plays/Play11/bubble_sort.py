# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 08:40:37 2019

@author: Margarida Viera
"""

def check(alist):
    for j in range(len(alist) - 1):
        if alist[j + 1] < alist[j]:
            return False
    return True
    
def bubble_sort(alist):
    
    if check(alist) == True:
        return alist
    
    for i in range(len(alist) - 1):
        if alist[i + 1] < alist[i]:
            value1 = alist[i]
            value2 = alist[i + 1]
            alist[i] = value2
            alist[i + 1] = value1
            
    return bubble_sort(alist)

print(bubble_sort(['Joaquina', 'Alexandra', 'Delfina', 'Emílio', 'Eduardo', 'Correia', 'João', 'Lopes']))