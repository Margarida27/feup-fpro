# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:53:37 2019

@author: Margarida Viera
"""

def greatest(num):
    num = str(num)
    num = list(num)
    output = ''
    num.sort(reverse = True)
    for n in num:
        output += n
    output = int(output)
    return output

print(greatest(310909))
print(greatest(7187))
print(greatest(99))
print(greatest(50710))
            
        
        
        