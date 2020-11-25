# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:52:13 2019

@author: Margarida Viera
"""

def override(l1, l2):
    override = sorted(l2 + list(filter(lambda x: x[0] not in map(lambda x: x[0], l2), l1)))
    return override

print(override([('a', 'b'), ('c', 'd')], [('b', 'a'), ('d', 'c')]))