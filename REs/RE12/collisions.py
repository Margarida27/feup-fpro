# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:55:41 2019

@author: Margarida Viera
"""

def number_of_collisions(objects):
    col = 0
    for i in range(0, len(objects) - 1):
        a = objects[i]
        for j in range(i + 1, len(objects)):
            b = objects[j]
            if b['y2'] < a['y1'] or b['y1'] > a['y2'] or b['x2'] < a['x1'] or b['x1'] > a['x2']:
                pass
            else:
                col += 1
    return col

print(number_of_collisions([{'x1': 11, 'y1': 192, 'x2': 59, 'y2': 280}, {'x1': 546, 'y1': 564, 'x2': 629, 'y2': 580}, {'x1': 368, 'y1': 418, 'x2': 455, 'y2': 432}, {'x1': 479, 'y1': 506, 'x2': 577, 'y2': 521}, {'x1': 113, 'y1': 315, 'x2': 156, 'y2': 415}, {'x1': 513, 'y1': 40, 'x2': 537, 'y2': 119}, {'x1': 521, 'y1': 488, 'x2': 549, 'y2': 522}, {'x1': 72, 'y1': 295, 'x2': 122, 'y2': 343}, {'x1': 87, 'y1': 160, 'x2': 135, 'y2': 213}, {'x1': 495, 'y1': 304, 'x2': 524, 'y2': 339}]))
    
