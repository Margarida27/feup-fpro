# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:04:26 2019

@author: Margarida Viera
"""

def to_fahrenheit(t):
    return list(map(lambda x: round((float(9 / 5) * x + 32), 2), t))

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))