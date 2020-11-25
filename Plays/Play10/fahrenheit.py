# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:38:42 2019

@author: Margarida Viera
"""

def to_fahrenheit(t):
    return [round((float(9 / 5) * x + 32), 2) for x in t]

print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]	))