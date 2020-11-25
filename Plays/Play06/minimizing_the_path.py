# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:35:19 2019

@author: Margarida Viera
"""
    
def min_path(path):
    redundant = {'UP':'DOWN', 'DOWN':'UP', 'LEFT':'RIGHT', 'RIGHT':'LEFT'}
    steps = []
    for step in path:
        if len(steps) != 0 and redundant[step] == steps[-1]:
            steps.pop()
        else:
            steps.append(step)
    return steps  
   
print(min_path(['LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'UP', 'LEFT']))
