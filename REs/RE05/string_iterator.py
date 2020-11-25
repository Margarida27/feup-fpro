# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:05:30 2019

@author: Margarida Viera
"""

def rm_letter_rev(l, astr):
    final_str = ''
    for i in range(len(astr)-1, -1, -1):
        if not(astr[i] == l):
            final_str += astr[i]
    return final_str
            
astr = input('string: ')
l = input('letter to be removed: ')
print(rm_letter_rev(l, astr))

