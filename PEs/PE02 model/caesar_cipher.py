# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:30:03 2019

@author: Margarida Viera
"""

import math

def fibonacci(n):
    fn = (((1 + math.sqrt(5)) ** n) - ((1 - math.sqrt(5)) ** n)) / ((2 ** n) * math.sqrt(5))
    return int(fn)

def caesar(message):
    message = list(message)
    cipher = ''
    ix = 0
    for char in message:
        if char == ' ':
            cipher += ' '
        elif 64 < ord(char) < 91:
            code = fibonacci(ix) 
            new_char = chr((((ord(char) - 65) - code) % 26) + 65)
            cipher += new_char
        else:
            cipher += char
        ix += 1
    return cipher
            
print(caesar('HELLO WORLD!'))
print(caesar('CAESAR CIPHER'))
print(caesar('FIBONACCI SEQUENCE'))
print(caesar('SUPER IMPORTANT MESSAGE!'))
        