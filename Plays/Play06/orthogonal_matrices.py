# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:57:47 2019

@author: Margarida Viera
"""

def mult(M, N):
    result = [[0 for row in range(len(N[0]))] for col in range(len(M))]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(M[0])):
                result[i][j] += M[i][k] * N[k][j] 
    return result

def is_orthogonal(mx):
    mt = list(zip(*mx))
    mi = [[1, 0],[0, 1]]
    if mult(mx, mt) == mi:
        return True
    else:
        return False
    
print(is_orthogonal([[-2, 3], [4, -1]]))
print(is_orthogonal([[1, 0], [0, -1]]))
    
    