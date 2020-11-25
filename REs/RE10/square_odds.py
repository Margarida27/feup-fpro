# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:25:09 2019

@author: Margarida Viera
"""

def square_odds(values):
    return ','.join([str(int(i) ** 2) for i in values.split(',') if int(i) % 2 == 1])

print(square_odds('1,2,3,4,5,6,7,8,9'))