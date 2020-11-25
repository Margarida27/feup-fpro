# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:54:03 2019

@author: Margarida Viera
"""

tS = float(input('Swimming stage time: '))
tC = float(input('Cycling stage time: '))
tR = float(input('Running stage time: '))

vS = 1.5 / tS
vC = 40 / tC
vR = 10 / tR

total_time = tS + tC + tR

for i in range(1):
    if not(vS < 2) and not(vC < 20) and not(vR < 8) and not(total_time > 4):
        print(total_time)
    elif total_time > 4:
        print('Time')
        break
    elif vS < 2:
        print('Swimming')
        break
    elif vC < 20:
        print('Cycling')
        break
    elif vR < 8:
        print('Running')
        break