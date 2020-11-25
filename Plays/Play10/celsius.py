# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:37:12 2019

@author: Margarida Viera
"""

def to_celsius(t):
    return [round((float(5 / 9)) * (x - 32), 1) for x in t]

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))