# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:14:13 2019

@author: Margarida Viera
"""

def count_chars(astring):
    alphabetic = 0
    digits = 0
    symbols = 0
    for char in astring:
        if ord(char) >= 48 and ord(char) <= 57:
            digits += 1
        elif (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            alphabetic += 1
        elif (ord(char) >= 33 and ord(char) <= 47) or (ord(char) >= 58 and ord(char) <= 64) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 91 and ord(char) <= 96) or (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 123 and ord(char) <= 127):
            symbols += 1
    output = (alphabetic, digits, symbols)
    return output

print(count_chars('Str1nG$'))
print(count_chars('Hello-2019-World'))
