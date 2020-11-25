# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:30:30 2019

@author: Margarida Viera
"""

def dogs(h_age):
    if h_age <= 2:
        dog_age = h_age * 10.5
    elif h_age > 2:
        dog_age = 2 * 10.5 + (h_age - 2) * 4
    return dog_age

print(dogs(3))