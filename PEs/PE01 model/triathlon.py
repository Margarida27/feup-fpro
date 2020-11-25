# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 15:07:30 2019

@author: Margarida Viera
"""

tS = float(input('swimming stage time: '))
tC = float(input('Cycling stage time: '))
tR = float(input('Running stage time: '))
t_total = tS + tC + tR

vS = 1.5 / tS
vC = 40 / tC
vR = 10 / tR

for i in range(1):
    if not(vS < 2) and not(vC < 20) and not(vR < 8) and not(t_total > 4):  
        print(t_total)
    elif t_total > 4:
        print('Time')
        break
    elif vS < 1.5:
        print('Swimming')
        break
    elif vC < 40:
        print('Cycling')
        break
    elif vR < 10:
        print('Running')
        break
