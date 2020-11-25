# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:37:50 2019

@author: Margarida Viera
"""

import math

def pascal(n):
    string = ''
    for i in range(n):
        for j in range(i + 1):
            element = int(math.factorial(i) / (math.factorial(j) * (math.factorial(i - j))))
            string += str(element) + ' '
        string = string.strip()    
        string += '\n'
    return string
    
print(pascal(3))
print(pascal(5))
print(pascal(1))
