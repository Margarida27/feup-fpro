# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:47:38 2019

@author: Margarida Viera
"""

integers = input()
reals = input()

if integers == [] and reals == []:
    output = ''
elif integers != [] and reals != []:
    output = ''
    for i in range(len(integers)):
        if integers[i] == reals[i]:
            output += ' ' + str(integers[i]) 
        elif integers[i] < reals[i]:
            output += ' ' + str(reals[i])
        elif integers[i] > reals[i]: 
            output += ' ' + str(integers[i])
            
print(output)

