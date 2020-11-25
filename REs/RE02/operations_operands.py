# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:12:33 2019

@author: Margarida Viera
"""
money = int(input())
payment_frequency = int(input())
interest_rate = float(input())
final_amount = money * ((1 + (interest_rate / payment_frequency)) ** (payment_frequency * 2))
print(round(final_amount, 3))

