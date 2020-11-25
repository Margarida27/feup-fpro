# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:33:20 2019

@author: Margarida Viera
"""

def academy_awards(alist):
    dict1 = {}
    for categorie in alist:
        if categorie[1] in dict1:
            dict1[categorie[1]] += 1
        else:
            dict1[categorie[1]] = 1
    return dict1

print(academy_awards([('Best Picture', 'Moonlight'), ('Best Director', 'La La Land'), ('Best Actor', 'Manchester by the Sea'), ('Best Actress', 'La La Land'), ('Best Supporting Actor', 'Moonlight'), ('Best Supporting Actress', 'Fences'), ('Best Original Screenplay', 'Manchester by the Sea'), ('Best Original Score', 'La La Land')]))