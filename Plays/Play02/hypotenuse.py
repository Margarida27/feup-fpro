# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:30:55 2019

@author: Margarida Viera
"""

import math 
def hypotenuse(n):
    hypotenuse = math.sqrt(n**2 + n**2)
    return round(hypotenuse, 2)

n = float(input())
print(hypotenuse(n))