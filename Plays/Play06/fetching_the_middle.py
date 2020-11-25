# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:19:47 2019

@author: Margarida Viera
"""

from math import floor

def fetch_middle(llists):
    middle = []
    for l in llists:
        if len(l) % 2 == 0:
            ix = int((len(l) / 2))
            mid = (l[ix - 1] + l[ix]) / 2
            middle.append(mid)
        else:
            ix = floor(len(l) / 2)
            mid = l[ix]
            middle.append(mid)
    return middle

print(fetch_middle([[10, 25, 35, 45], [100, -1, 3, 4], [-3, -5, -10, -20, -100]]))
            