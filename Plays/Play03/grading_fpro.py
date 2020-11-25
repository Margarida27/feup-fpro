# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:38:47 2019

@author: Margarida Viera
"""

le = input()
re = input()
pe = input()
te = input()
if not (0 <= le <= 100 and 0 <= re <= 100 and 0 <= pe <= 100 and 0 <= pe <= 100):
    print ('Input error')
elif (pe < 40) or (te < 40):
    print ('RFC')
else:
    grade = (le + re + 5 * pe + 3 * te) / 50
    print (int(grade + 0.5))