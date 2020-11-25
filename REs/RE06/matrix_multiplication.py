# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:52:55 2019

@author: Margarida Viera
"""

def mult(M, N):
    if len(M[0]) != len(N):
        return []
    else:
        result = [[0 for row in range(len(N[0]))] for col in range(len(M))]
            
        for i in range(len(M)):
           for j in range(len(N[0])):
               for k in range(len(M[0])):
                   result[i][j] += M[i][k] * N[k][j] 
    return result

print(mult([[0, 1, 2], [2, 1, 0], [4, 1, 3], [1, 6, -2]], [[2, 1], [7, 8], [2, -10]]))
print()
print(mult([[2, 1], [7, 8], [2, -10]], [[2, 1, 8, 10, -2], [7, 8, -2, -6, 10]]))
print()
print(mult([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[2, 1, 5], [7, 8, 10], [2, -10, -2], [-8, 10, 1], [-4, 6, 7]]))
print()
print(mult([[-7, 8, -10], [1, -4, 7]], [[2, -1], [7, -8], [-2, 10]]))
        