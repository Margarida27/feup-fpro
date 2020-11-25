# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:33:23 2019

@author: Margarida Viera
"""

def check(string):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for letter in abc:
        if letter in string:
            check = True
        else:
            check = False
            break
    return check
        
def complete_pairs(s1, s2):
    complete = []
    for str1 in s1:
        for str2 in s2:
            if check(str1 + str2) == True:
                complete.append(str1 + str2)
    return set(complete)

print(complete_pairs({'abcdefgh', 'geeksforgeeks', 'lmnopqrst', 'abc'}, {'abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstuvwxyz', 'defghijklmnopqrstuvwxyz'}))