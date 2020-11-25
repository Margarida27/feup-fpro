# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 19:53:09 2019

@author: Margarida Viera
"""

def binary_tree(key, tree):
    trial, value, left, right = tree
    if key == trial:
        return value
    else:
        try:
            left()
            return binary_tree(key, left())
        except:
            right()
            return binary_tree(key, right())
        
#other solution       
def binary_tree(key, tree):
    key_, value, left, right = tree
    while key != key_:
        if key > key_:
            (key_, value, left, right) = right()
        elif key < key_:
            (key_, value, left, right) = left()
    return value

print(binary_tree('hummer', ('aptitudes', 495, lambda: 1/0, lambda: ('roadblock', 25, lambda: ('paramedic', 211, lambda: ('bizets', 115, lambda: 1/0, lambda: ('modernizes', 848, lambda: ('lees', 937, lambda: ('gusty', 472, lambda: 1/0, lambda: ('haggles', 648, lambda: 1/0, lambda: ('jaclyns', 170, lambda: ('implication', 297, lambda: ('hummer', 561, lambda: 1/0, lambda: 1/0), lambda: 1/0), lambda: 1/0))), lambda: 1/0), lambda: 1/0)), lambda: 1/0), lambda: 1/0))))