# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 09:29:43 2019

@author: Margarida Viera
"""

import random 

def bulls_cows(seed):
    random.seed(seed)
    num = random.randrange(0,10000)
    
    def closure(guess):
        guess1 = list(str(guess))
        check = list(str(num))
        guess = str(guess)
        num1 = str(num)
        cows = 0
        bulls = 0
        
        for i, n in enumerate(num1):
            if n == guess[i]:
                cows += 1
                guess1.remove(n)
                check.remove(n)
                
        for i in guess1:
            if i in check:
                bulls += 1
                check.remove(i)
                
        return (cows,bulls)
    
    return closure

print(bulls_cows(510))
        
        
    
    