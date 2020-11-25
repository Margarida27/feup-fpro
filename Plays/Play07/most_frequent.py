# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:42:22 2019

@author: Margarida Viera
"""

  
def most_frequent(alist): 
    dict1 = {} 
    count, num = 0, '' 
    for n in alist: 
        dict1[n] = dict1.get(n, 0) + 1
        if dict1[n] >= count: 
            count, num = dict1[n], n
    return num

print(most_frequent([-1, 111, 1, 11, -1, 11, 1, 111]))
        