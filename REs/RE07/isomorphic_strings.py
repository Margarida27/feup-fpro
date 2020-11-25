# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:11:35 2019

@author: Margarida Viera
"""

def isomorphic(astring1, astring2):
    if len(astring1) != len(astring2):
        return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
    letters1 = []
    letters2 = []
    for letter in astring1:
        if letter not in letters1:
            letters1.append(letter)
    for letter in astring2:
        if letter not in letters2:
            letters2.append(letter)
    if len(letters1) != len(letters2):
        return "'{0}' and '{1}' are not isomorphic".format(astring1, astring2)
    else:
        dict1 = {}
        for i in range(len(letters1)):
            dict1[letters1[i]] = letters2[i]
        output = "'{0}' and '{1}' are isomorphic because we can map: ".format(astring1, astring2)
        maps = []
        for key in dict1:
            maps.append((key, dict1[key]))
        output += str(maps)
        return output
    
print(isomorphic('paper', 'title'))

    
    
        