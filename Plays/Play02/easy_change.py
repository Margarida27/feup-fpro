# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 23:03:07 2019

@author: Margarida Viera
"""

def easy_change(price, received):
    change = received - price 
    n50 = 0
    n20 = 0
    n10 = 0
    n5 = 0
    while change >= 50:
        change = change - 50
        n50 += 1
    while change >= 20:
        change = change - 20
        n20 += 1
    while change >= 10:
        change = change - 10
        n10 += 1
    while change >= 5:
        change = change - 5
        n5 += 1
    n = str(n50) + ' ' + str(n20) + ' ' + str(n10) + ' ' + str(n5)
    return n
price = int(input()) 
received = int(input())
print(easy_change(price, received))