# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 22:22:36 2019

@author: Margarida Viera
"""

import math

def time_until_lost_connection(direction_A, direction_B):
    alfa = (abs(direction_B - direction_A) * math.pi) / 180
    hours = (math.sqrt(1225 / (2 - (2 * math.cos(alfa))))) / 5
    time_until_lost_connection = (hours * 60)
    return round(time_until_lost_connection, 3)
  

#---comment section---
#((5 * time) **2) + ((5 * time) **2) - 2 * ((5 * time) **2) * math.cos(alfa) = 1225 (35**2) (lei dos cossenos)
#((5 * time) **2)(1 + 1 - 2 * math.cos(alfa)) = 1225
#((5 * time) **2) = 1225 / (2 - 2 * math.cos(alfa))
#(5 * time) = sqrt(1225 / (2 - 2 * math.cos(alfa)))
# time = (sqrt(1225 / (2 - 2 * math.cos(alfa)))) / 5
# a partir da equação acima obtemos o tempo expresso em hora - hours
