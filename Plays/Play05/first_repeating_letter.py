# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:50:32 2019

@author: Margarida Viera
"""

def repeated_letter(s):
    s = list(s)
    index = 1
    for x in s:
        p = s[index:]
        for y in p:
            if x == y:
                letter = x
                return letter
                break
        index += 1
        
print(repeated_letter('tweet'))
print(repeated_letter('like'))
print(repeated_letter('patricia'))
print(repeated_letter('internet'))


            