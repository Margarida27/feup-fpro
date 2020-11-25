# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:56:00 2019

@author: Margarida Viera
"""

def roman_to_integer(astring):
    dict_roman = {}
    dict_roman['I'] = 1
    dict_roman['V'] = 5
    dict_roman['X'] = 10
    dict_roman['L'] = 50
    dict_roman['C'] = 100
    dict_roman['D'] = 500
    dict_roman['M'] = 1000
    roman = astring
    decimal = 0
    for r in range(len(roman) - 1):
        if dict_roman[roman[r]] >= dict_roman[roman[r + 1]]:
            decimal += dict_roman[roman[r]]
        else:
            decimal -= dict_roman[roman[r]]
    decimal += dict_roman[roman[-1]]
    return decimal

print(roman_to_integer('MMMCMXCIX'))
            