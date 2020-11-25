# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:40:12 2019

@author: Margarida Viera
"""

def map(pos, steps):
    pos = list(pos)
    left_right = pos[0]
    up_down = pos[1]
    steps = steps.split('-')
    for step in steps:
        if step == 'up':
            up_down += 1
        elif step == 'down':
            up_down -= 1
        elif step == 'right':
            left_right += 1
        elif step == 'left':
            left_right -= 1
    final_pos = (left_right, up_down)
    return final_pos

print(map((0, 0), 'up-up-left-right-up-up'))
print(map((0, 4), 'up-up-left-left-up-up'))
print(map((0, 0), 'down-left-down-left-up-right-right-up'))
print(map((8, 4), 'down-down-left-left-up-up'))


