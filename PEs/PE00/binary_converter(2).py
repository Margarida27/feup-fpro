# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:18:41 2019

@author: Margarida Viera
"""

n = int(input())
binary = ''
while n > 0:
    bit = n % 2
    n //= 2
    binary += str(bit)
binary_ = '' #the final binary value will be assign to this variable 
for i in range((len(binary) - 1), -1, -1): 
    binary_ += binary[i]
binary_ = int(binary_)
print(binary_)

#>>>>>another possible code:<<<<<
#num = int(input())
#num = bin(num)
#num = num.lstrip('-0b')
#print(num)