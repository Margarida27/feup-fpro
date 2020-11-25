# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:16:20 2019

@author: Margarida Viera
"""

def histogram(alist, bins):
    freq = []
    for i in range(len(bins) - 1):
        interval = range(bins[i], bins[i + 1])
        count = 0
        for n in alist:
            if n in interval:
                count += 1
        freq.append(count)
        
    return freq

print(histogram([0, 3, 4, 7, 8, 1, 5], (0, 3, 7, 12)))
                
        