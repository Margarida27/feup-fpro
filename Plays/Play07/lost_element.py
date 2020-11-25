# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:37:03 2019

@author: Margarida Viera
"""

def lost_element(s1, s2):
    if len(s1) > len(s2):
        for n in s1:
            if n not in s2:
                return n
    if len(s2) > len(s1):
        for n in s2:
            if n not in s1:
                return n

print(lost_element({1, 4, 5, 7, 9}, {9, 4, 5, 7}))
