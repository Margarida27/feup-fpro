# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:32:40 2019

@author: Margarida Viera
"""

def sort_rule(item):
    mean = float(sum(item[2]) / max(len(item[2]), 1))
    mean = 100 - mean
    return (mean, item[0], item[1])
    
def sort_grades(records):
    return tuple(sorted(records, key = sort_rule, reverse = False))
    
