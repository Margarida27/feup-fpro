# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:41:26 2019

@author: Margarida Viera
"""

def sparse_dot_product(dict1, dict2):
    product = 0
    for key in dict1:
        if key in dict2:
            product += dict1[key] * dict2[key]
    return product

print(sparse_dot_product({2: 90, 9: 80, 1: -5, 8: 7}, {2: -4, 9: 1, 1: 6}))
            