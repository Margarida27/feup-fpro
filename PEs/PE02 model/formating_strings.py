# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:21:02 2019

@author: Margarida Viera
"""

def exactly(s):
    tup = ()
    for x in range(len(s)):
        for y in range(x + 1, len(s)):
            if s[x].isdigit() and s[y].isdigit() and int(s[x]) + int(s[y]) == 10:
              question_mark = s[x + 1:y]  
              if question_mark.count('?') == 3:
                  tup += (s[x] + s[y],)
              else:
                  tup += (s[x] + s[y],)
                  return 'The sequence {0} is NOT OK with first violation with pair: {1}'.format(s, tup)
    return 'The sequence {0} is OK with the pair: {1}'.format(s, tup)
                                   
print(exactly('acc?7??sss?3rr1??????5???5'))
print()
print(exactly('acc?7??sss3rr1??????5'))
print()
print(exactly('aa6?9'))
print()
print(exactly('htrtr24?h56h56??29004??34'))
                    
    
                    
                    
        