# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:44:13 2019

@author: Margarida Viera
"""

import math
def average(a, b):
    average = math.ceil((a + b) / 2)
    return average

def digits_average(n):
    if n < 10:
        return n
    else:
        t = n
        x = 1 #x gives the number of digits
        while t // 10 != 0:
            t = t // 10
            x += 1
        
        while n > 9:
            while n > 9: 
                a = 0
                for i in range(0, x - 1):
                    d1 = n % 10
                    n = n // 10
                    d2 = n % 10
                    a = average(d1, d2) * (10 ** i) + a
            n = a
            t = n
            x = 1 #x gives the number of digits
            while t // 10 != 0:
                t = t // 10
                x += 1
        return a       

        
        
    
    
    
    

    