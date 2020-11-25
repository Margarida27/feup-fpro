# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:11:26 2019

@author: Margarida Viera
"""

def anagrams(alist):
    listwords = {}
    for x in alist:
        y = x.lower()
        y = sorted(y)
        while ' ' in y:
            y.remove(' ')
        y = str(y)
        if y in listwords:
            listwords[y].append(x)
        else:
            listwords[y] = [x]
    listwords = list(listwords.values())
    for x in range(len(listwords)):
        listwords[x] = sorted(listwords[x])
    listwords = sorted(listwords, key = lambda stu: stu[0].lower())
    return listwords

print(anagrams(['they see', 'eat', 'The eyes', 'car has', 'ate', 'a crash', 'tea']))
print()
print(anagrams(['sentence', 'lives', 'ten scene', 'bat', 'Elvis', 'CE sennet']))
print()
print(anagrams(['William Shakespeare', 'I am a weakish speller', 'Madam Curie', 'Radium came']))
print()
print(anagrams(['funeral', 'restful', 'fluster', 'apple', 'real fun']))
print()   
print(anagrams(['ferrari', 'Elon Musk', 'Muskmelon', 'rrarife', 'tenerife']))
print() 
print(anagrams(['Edward Gorey', 'Ogdred Weary', 'Regera Dowdy', 'E G Deadworry']))
