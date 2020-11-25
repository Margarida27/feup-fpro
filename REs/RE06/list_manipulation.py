# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:04:39 2019

@author: Margarida Viera
"""

def manipulator(l, cmds):
    result = ''
    for cmd in cmds:
        l_cmd = cmd.split()
        if cmd == []:
            result += []
        elif len(l_cmd[0]) < 3:
            result += cmd + ' '
        elif l_cmd[0] == 'insert':
            i = int(l_cmd[1])
            e = int(l_cmd[2])
            l.insert(i, e)
        elif l_cmd[0] == 'remove':
            r = int(l_cmd[1])
            if r in l:
                l.remove(r)
        elif l_cmd[0] == 'append':
            a = int(l_cmd[1])
            l.append(a)
        elif l_cmd[0] == 'sort':
            l.sort()
        elif l_cmd[0] == 'pop':
            if l != []:
                l.remove(l[-1])
        elif l_cmd[0] == 'reverse':
            l.reverse()
        elif l_cmd[0] == 'print':
            result += str(list(l)) + ' '
    return result
            
print(manipulator([2, 4], ['print', 'remove 4', 'append 1', 'sort', 'print', 'pop', 'reverse', 'print']))
          
            
            
            
        