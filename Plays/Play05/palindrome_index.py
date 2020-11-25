# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 12:43:08 2019

@author: Margarida Viera
"""

def palindrome_index(s):
    s = list(s)
    p = list(s)
    if s == s[::-1]:
        return -1
    else:
        index = 0
        for letter in s:
            p.remove(letter)
            if p == p[::-1]:
                output = index
                break
            else:
                output = -1
            index += 1
            p = list(s)
        return output
            


print(palindrome_index('aaab'))
print(palindrome_index('tattarrattat')) 
print(palindrome_index('acbddba')) 
print(palindrome_index('abba'))         
            