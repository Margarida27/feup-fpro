# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:22:50 2019

@author: Margarida Viera
"""

def change(money):
    coins = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    
    for key in coins:
        coins[key] = money // key
        money = round(money % key, 2)
        
    return coins

print(change(7.71))