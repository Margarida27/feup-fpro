# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:19:40 2019

@author: Margarida Viera
"""

def split(alist):
    alist.sort()
    size = len(alist) // 2
    L = alist[:size]
    R = alist[size:]
    return L, R

from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) 

def closest_pair(points):
    
    points = sorted(points, key = lambda x: x[0])
    L, R = split(points)
    
    dists = []
    
    for p in range(len(L) - 1):
        dists.append(distance(L[p], L[p + 1]))

    for p in range(len(R) - 1):
        dists.append(distance(R[p], R[p + 1]))

    for p in range(len(L)):
        dists.append(distance(L[p], R[p]))

    return round(min(dists))

print(closest_pair([(1256, 8483), (61, 2321), (9442, 4823), (1940, 700)]))
    
    
    