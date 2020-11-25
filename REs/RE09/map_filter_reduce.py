# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:55:30 2019

@author: Margarida Viera
"""

from functools import reduce 

def reduce_map_filter(args):
    if type(args[2]) == list:
        if args[0] == 'map':
             return list(map(args[1], args[2]))
        elif args[0] == 'filter':
            return list(filter(args[1], args[2]))
        elif args[0] == 'reduce':
            return reduce(args[1], args[2])
        
    else:
        if args[0] == 'map':
             return list(map(args[1], reduce_map_filter(args[2])))
        elif args[0] == 'filter':
            return list(filter(args[1], reduce_map_filter(args[2])))
        elif args[0] == 'reduce':
            return reduce(args[1], reduce_map_filter(args[2]))
        
print(reduce_map_filter(('reduce', lambda a,b: a+b, ('map', lambda x: 2*x, ('filter', lambda x: x%2 != 0, [1, 2, 3])))))