# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 20:33:53 2019

@author: Margarida Viera
"""

import math

def fibonacci(n):
    """
    determines the fibonnaci's sequence number to be applied in order to cipher a certain word index
    """
    fn = (((1 + math.sqrt(5)) ** n) - ((1 - math.sqrt(5)) ** n)) / ((2 ** n) * math.sqrt(5))
    return int(fn)

def index(l):
    """
    determines the position of a given letter in the alphabet (letters list)
    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index = 0
    for letter in letters:
        if l != letter:
            index += 1
        else:
            break
    return index

def special_char(l):
    """
    determines if a character exists on the list
    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for letter in letters:
        check = letter == l
        if check == True:
            return True
    if check == False:
        return False          
    
def caesar(message):
    """
    ciphers a certain string given by input
    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    string = ''
    for n in range(len(message)):
        for letter in letters:
            if special_char(message[n]) == False:
                string += message[n]
                break
            elif message[n] == letter:
                    letters_index = (index(letter) - fibonacci(n)) % 26
                    string += letters[letters_index]
    return string

print(caesar('HELLO WORLD!'))        
print(caesar('CAESAR CIPHER'))
print(caesar('FIBONACCI SEQUENCE'))  
print(caesar('SUPER IMPORTANT MESSAGE!'))  
     