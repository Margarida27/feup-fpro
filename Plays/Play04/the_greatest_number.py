# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:53:53 2019

@author: Margarida Viera
"""

#def greatest(num):
#    num = str(num)
#    num = list(num)
#    output = ''
#    for x in num:
#        for y in num:
#            if y > x:
#                greatest = y
#                num.remove(str(greatest)) 
#                output += str(greatest)
#    for x in num:
#        for y in num:
#            if y == x:
#                greatest = x
#                num.remove(str(x)) 
#                output += str(x)
#    if len(num) != 0:
#        for z in num:
#            output += str(z)
#    output = int(output)
#    return output

def greatest(num):
    num = str(num)
    num = list(num)
    num_list = sorted(num, reverse = True)
    output = ''
    for num in num_list:
        output += num
    output = int(output)
    return output

print(greatest(310909))
print(greatest(7187))
print(greatest(99))
print(greatest(50710))


            