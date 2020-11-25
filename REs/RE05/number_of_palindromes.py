# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:12:08 2019

@author: Margarida Viera
"""

def palindrome(astring):
    count = 0
    for x in range(len(astring) + 1):
        for y in range(x + 2, len(astring) + 1):
            substring = astring[x:y]
            reverse = substring[::-1]
            if reverse == substring:
                count += 1
    output = 'The string {0} contains {1} palindrome substrings.'.format(astring, count)
    return output

print(palindrome('geek'))
print(palindrome('ababa'))
print(palindrome('abbaeae'))
print(palindrome('nope'))
