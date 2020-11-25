# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 13:00:11 2019

@author: Margarida Viera
"""

def to_celsius(t):
    return list(map(lambda x: round((float(5 / 9)) * (x - 32), 1), t))

print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))
