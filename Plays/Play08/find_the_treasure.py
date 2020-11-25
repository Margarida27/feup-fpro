# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 10:52:46 2019

@author: Margarida Viera
"""

def map(pos, steps):
    pos = list(pos)
    if steps == []:
        return tuple(pos)
    else:
        if steps[0] == 'right':
            pos[0] += 1
        elif steps[0] == 'left':
            pos[0] -= 1
        elif steps[0] == 'up':
            pos[1] += 1
        elif steps[0] == 'down':
            pos[1] -= 1
        return map(pos, steps[1:])

print(map((0, 4), ['up', 'up', 'left', 'left', 'up', 'up']))
