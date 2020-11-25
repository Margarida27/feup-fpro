# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:55:01 2019

@author: Margarida Viera
"""

def summary_ranges(astring):
    astring = list(map(int, astring.split(',')))
    intervals = []
    while len(astring) != 0:
        prev_bound = astring[0]
        next_bound = astring[0]
        for i,elem in enumerate(astring):
            if elem == prev_bound + i:
                next_bound = elem
            else:
                intervals.append(convert_interval([prev_bound, next_bound]))
                astring = astring[i:]
                break
        else:
            intervals.append(convert_interval([prev_bound, next_bound]))
            astring = ''
            break
    return ','.join(intervals)
def convert_interval(interval):
    return f'{interval[0]}->{interval[1]}' if interval[0] != interval[1] else str(interval[0])

                
print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))

               