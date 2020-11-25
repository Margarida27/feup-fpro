# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:30:29 2019

@author: Margarida Viera
"""


def adigits(d1, d2, d3):
    if d1 > d2 and d1 > d3:
        centenas = d1
        if d2 > d3:
            dezenas = d2
            unidades = d3
        else:
            dezenas = d3
            unidades = d2
    elif d2 > d1 and d2 > d3:
        centenas = d2
        if d1 > d3:
            dezenas = d1
            unidades = d3
        else:
            dezenas = d3
            unidades = d1
    elif d3 > d1 and d3 > d2:
        centenas = d3
        if d1 > d2:
            dezenas = d1
            unidades = d2
        else:
            dezenas = d2
            unidades = d1
    adigits = str(centenas) + str(dezenas) + str(unidades)
    return adigits



