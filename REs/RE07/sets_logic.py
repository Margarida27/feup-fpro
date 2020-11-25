# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:35:18 2019

@author: Margarida Viera
"""

def logic(s, operations):
    for key in operations:
        if key == 'or':
            s = set(operations[key]).union(s)
        elif key == 'and':
            s = set(operations[key]).intersection(s)
        elif key == 'not':
           s = set(operations[key]).difference(s)
        elif key == 'xor':
            s = set(operations[key]).symmetric_difference(s)
    return s

print(logic({1, 2, 3, 4}, {'xor': {0, 3, 4}, 'not': {0, 1, 2, 3, 4, 5, 6}}))
