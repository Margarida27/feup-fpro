# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 18:41:20 2019

@author: Margarida Viera
"""

def remove_leading(ip):
    ip = ip.split('.')
    output = []
    for y in ip:
        y = int(y)
        y = str(y)
        output.append(y)
    return '.'.join(output)
          
print(remove_leading('255.024.01.01'))
print(remove_leading('192.168.0.24'))
print(remove_leading('00.0.0000.0'))
print(remove_leading('127.56.10.100'))