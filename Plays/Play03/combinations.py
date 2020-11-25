# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:33:50 2019

@author: Margarida Viera
"""

#def C(n, r):
#    t = n - r
#    for i in range(1,n):
#        n *= i    
#    for i in range(1, r):
#        r *= i
#    if t == 0:
#        t = 1
#    else:
#        for i in range(1, t):
#            t *= i
#    return(round(n / (r * t)))

def C(n, r):
    t = n - r
    for i in range(n-1,0,-1):
        n *= i    
    for i in range(r-1,0,-1):
        r *= i
    if t == 0:
        t = 1
    else:
        for i in range(t-1,0,-1):
            t *= i
    return(round(n / (r * t)))

    



    
    

