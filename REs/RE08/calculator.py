# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 08:54:42 2019

@author: Margarida Viera
"""

def calculator(expr):
    if type(expr) is tuple:
        if expr[1] == '+':
            return calculator(expr[0]) + calculator(expr[2])
        elif expr[1] == '-':
            return calculator(expr[0]) - calculator(expr[2])
        elif expr[1] == '*':
            return calculator(expr[0]) * calculator(expr[2])
    else:
        return expr
    
print(calculator(((1, '+', 2), '*', 3)))