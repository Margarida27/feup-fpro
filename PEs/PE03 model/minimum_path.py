# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:19:32 2019

@author: Margarida Viera
"""

def min_path(mx, a, b, visited=[]):
    IMPOSSIBLE = 999999

    # a and b are at the same position, the distance between them equals to 0
    if a == b:
        return 0
    
    # a is not at any line of the matrix
    if a[0] < 0 or a[0] >= len(mx):
        return IMPOSSIBLE
    
    # a is not at any column of the matrix
    if a[0] < 0 or a[0] >= len(mx[0]):
        return IMPOSSIBLE
    
    # a is at an obstacle position
    if mx[a[0]][a[1]] is True:
        return IMPOSSIBLE
    
    # a is at an already visited place
    if a in visited:
        return IMPOSSIBLE
    
    dists = [
        1 + min_path(mx, (a[0]+1, a[1]), b, visited+[a]),
        1 + min_path(mx, (a[0]+1, a[1]-1), b, visited+[a]),
        1 + min_path(mx, (a[0]+1, a[1]+1), b, visited+[a]),
        1 + min_path(mx, (a[0]-1, a[1]), b, visited+[a]),
        1 + min_path(mx, (a[0]-1, a[1]-1), b, visited+[a]),
        1 + min_path(mx, (a[0]-1, a[1]+1), b, visited+[a]),
        1 + min_path(mx, (a[0], a[1]-1), b, visited+[a]),
        1 + min_path(mx, (a[0], a[1]+1), b, visited+[a]),
        ]
    
    return min(dists)

mx = mx = [
[False]*4,
[False, True, False, False],
[False, True, False, False],
[False]*4
]

print(min_path(mx, (2, 0), (0, 3)))
print()
print(min_path(mx, (3, 1), (0, 1)))
print()
print(min_path(mx, (0, 0), (3, 3)))
    
    
    
    
    
    
