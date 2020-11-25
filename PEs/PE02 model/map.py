# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:39:58 2019

@author: Margarida Viera
"""

def map(pos, steps):
    pos = list(pos)
    steps = steps.split('-')
    right_left = pos[0]
    up_down = pos[1]
    for step in steps:
        if step == 'up':
            up_down += 1
        elif step == 'down':
            up_down -= 1
        elif step == 'right':
            right_left += 1
        elif step == 'left':
            right_left -= 1
    return [right_left, up_down]

print(map((0, 0), 'up-up-left-right-up-up'))
print(map((0, 4), 'up-up-left-left-up-up'))
print(map((0, 0), 'down-left-down-left-up-right-right-up'))
print(map((8, 4), 'down-down-left-left-up-up'))
