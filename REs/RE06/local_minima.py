# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 22:56:41 2019

@author: Margarida Viera
"""

def local_minima(alist, n):
    n = n // 2
    final = []
    test = []
    
    for ind, num in enumerate (alist):
        if (ind - n) < 0:
            test = alist [:(ind + n + 1)]
            if num == min(test):
                final = final + [(num, ind)]
        else:
            test = alist[(ind - n):(ind + n + 1)]
            if num == min(test):
                final = final + [(num, ind)]
                    
    for i in range(1, n + 1):
        for j in range (len(final) - i):
            if final[j][0] == final[j + 1][0] and ((int(final[j][1]) + i) == int(final[j + 1][1])):
                final.remove(final[j + 1])
                break
            
    return final