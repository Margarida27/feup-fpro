# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:32:10 2019

@author: Margarida Viera
"""

import math

def solver(a, b, c):
    d = ((b ** 2) - 4 * a * c)
    if d < 0:
        return []
    else:
        alist = []
        solution_1 = ((b * -1) + math.sqrt(d)) / (2 * a)
        solution_2 = ((b * -1) - math.sqrt(d)) / (2 * a)
        if solution_1 == solution_2:
            alist.append(solution_1)
            return alist
        elif solution_1 < solution_2:
            alist.append(solution_1)
            alist.append(solution_2)
            return alist
        elif solution_1 > solution_2:
            alist.append(solution_2)
            alist.append(solution_1)
            return alist

print(solver(2, 5, -3))
print(solver(-2, -5, -3))

