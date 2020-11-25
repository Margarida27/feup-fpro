# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 00:19:28 2019

@author: Margarida Viera
"""

def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    else:
        alist = alist[((step - 1) % len(alist)):] + alist[:((step - 1) % len(alist))]
        alist.remove(alist[0])
        return last_man_standing(alist, step)
    
print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))
