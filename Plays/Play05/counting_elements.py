# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:29:28 2019

@author: Margarida Viera
"""

def check(tup):
    for elem in tup:
        check = type(elem).__name__ == 'tuple'
        if check == False:
            continue
        else:
            return True
            break
            
def count_until(tup):
    if check(tup) == True:
        count = 0
        for elem in tup:
            if type(elem).__name__ != 'tuple':
                count += 1
            else:
                break
        return count
    else:
        return -1       
   
print(count_until((1, '2', 3, 4.0, 5j)))
print(count_until((1, 2, (3,), 4.0, 5j)))


        