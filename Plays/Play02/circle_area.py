# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:24:15 2019

@author: Margarida Viera
"""

PI = 3.14159
def circle(r):
    circle = PI*r*r
    return round(circle, 2)
 
r = float(input())
print(circle(r))