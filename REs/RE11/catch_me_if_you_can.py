# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:58:49 2019

@author: Margarida Viera
"""

def find_me(f, limits):
    i = -1
    
    while True:
        guess = (limits[0] + limits[1]) // 2 
        i += 1
        
        if f(guess) == -1:
            limits = (limits[0], guess)
            
        if f(guess) == 1:
            limits = (guess, limits[1])
        
        if f(guess) == 0:
            return i
        
print(find_me(lambda n: -1 if n > 31 else 1 if n < 31 else 0, (0, 100)))

print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))
