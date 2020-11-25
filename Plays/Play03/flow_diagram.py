# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:45:16 2019

@author: Margarida Viera
"""

l = int(input())
s = int(input())
r = l

if not(r>s):
    l = r
    r = s
    s = l

while not(s>r):
    r = r-s

while not(r==0):
    l = r
    r = s
    s = l
    while not(s>r):
        r = r-s

if r == 0:
    print(s)