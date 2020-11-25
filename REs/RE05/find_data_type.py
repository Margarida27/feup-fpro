# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:22:49 2019

@author: Margarida Viera
"""

def find_dtype(atuple, data_type):
    final_tuple = ()
    for n in atuple:
        if str(type(n).__name__) == data_type:
            final_tuple = final_tuple[0:] + (n,) 
    return final_tuple
    
      
atuple = tuple(input('atuple: '))
data_type = input('data_type: ')
print(find_dtype(atuple, data_type))
