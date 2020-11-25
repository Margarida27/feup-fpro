# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:01:29 2019

@author: Margarida Viera
"""

def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    guess = g1 + g2 + g3
    key = c1 + c2 + c3
    for i in range(3):
        if guess[i] == key[i]:
            points += 3
        else:
            for n in range(1, 3):
                if guess[i] == key[n]:
                    points += 1
    return points

g1 = input()
g2 = input()
g3 = input()
c1 = input()
c2 = input()
c3 = input()
print(mastermind(g1, g2, g3, c1, c2, c3))


