# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:09:56 2019

@author: Margarida Viera
"""

def triplet(atuple):
    list1 = []
    a = 0
    b = 0
    c = 0
    for x in atuple:
        for y in atuple:
            if a == b:
                b += 1
                continue
            for z in atuple:
                if c == a or c == b:
                    c += 1
                    continue 
                if x + y + z == 0:
                    list1.append((x, y, z))
                c += 1
            b += 1
            c = 0
        a += 1
    if len(list1) == 0:
        return ()
    else:
        return list1[0]
                
                
                