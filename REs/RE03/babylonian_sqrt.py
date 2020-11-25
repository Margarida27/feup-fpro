# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:10:55 2019

@author: Margarida Viera
"""

num = float(input()) 
#num given by user input
x = num / 2 #my initial guess
y = (x + num / x) / 2 #my initial guess improved
z = (round(y, 2) - round(x, 2)) #difference between guesses
while z != 0: #convergence is achieved when the digits of x and y agree on 2 decial places (z == 0)
    y = (x + num / x) / 2
    x = y
    z = x - y
print(round(y, 2)) 


  