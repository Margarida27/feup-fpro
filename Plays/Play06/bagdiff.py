# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:15:34 2019

@author: Margarida Viera
"""

def bagdiff(xs, ys):
    output = []
    for n in xs:
        if n in ys:
            ys.remove(n)
        else:
            output.append(n)
    return output

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))
            