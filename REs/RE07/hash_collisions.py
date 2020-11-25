# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:45:11 2019

@author: Margarida Viera
"""

def collisions(alist):
    dict1 = {}
    for number in alist:
        number = str(number)
        add = 0
        for n in range(len(number)):
            add += int(number[n])
        hash_ = add % 8
        if hash_ in dict1:
            dict1[hash_] += 1
        else:
            dict1[hash_] = 1
    return dict1

print(collisions([1, 789, 100, 9807, 1208, 92, 101]))
        
            