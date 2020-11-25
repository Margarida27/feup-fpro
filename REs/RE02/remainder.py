# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:37:59 2019

@author: Margarida Viera
"""

import datetime
now = datetime.datetime.now()
hours = (now.hour + 8) % 24 
minutes = (now.minute + 30) % 60
hours = hours + minutes // 60
print(str(hours).zfill(2) + ':' + str(minutes).zfill(2))

