# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:28:34 2019

@author: Margarida Viera
"""

import math
s = 0
for k in range(0, 51):
    s = s + (math.factorial(4 * k) * (1103 + (26390 * k))) / ((math.factorial(k) ** 4) * (396) ** (4 * k))
inverso = (2 * math.sqrt(2) / 9801) * s
pi = 1 / inverso
print(round(pi ,8))







    