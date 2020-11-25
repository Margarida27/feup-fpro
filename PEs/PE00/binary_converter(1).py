# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:51:23 2019

@author: Margarida Viera
"""

num = int(input())
num = bin(num)
num = num.lstrip('-0b')
print(num)