# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:26:14 2019

@author: Margarida Viera
"""

             
def move_ball(board):
    b = board
           
    for i in range(len(b)): # lines
        for j in range(len(b[0])):  # columns
            if b[i][j] == 'X':
                end = (i,j)
            if b[i][j] in ['N','S','E','W']:
                pos = (i,j)
                ball = b[i][j]
                
    path = []
    path.append(pos)
    x,y = pos[0],pos[1]
        
    while end not in path:
       
        if ball == 'N':
            pos = (x-1,y)
            x,y = pos[0],pos[1]
            path.append(pos)
            if b[x][y] == '\\':
                ball = 'W'
            elif b[x][y] == '/':
                ball = 'E'
            elif b[x][y] == ' ':
                ball = ball
                            
        elif ball == 'S':
            pos = (x+1,y)
            x,y = pos[0],pos[1]
            path.append(pos)
            if b[x][y] == '\\':
                ball = 'E'
            elif b[x][y] == '/':
                ball = 'W'
            elif b[x][y] == ' ':
                ball = ball
        
        elif ball == 'E':
            pos = (x,y+1)
            x,y = pos[0],pos[1]
            path.append(pos)
            if b[x][y] == '\\':
                ball = 'S'
            elif b[x][y] == '/':
                ball = 'N'
            elif b[x][y] == ' ':
                ball = ball
        
        elif ball == 'W':
            pos = (x,y-1)
            x,y = pos[0],pos[1]
            path.append(pos)
            if b[x][y] == '\\':
                ball = 'N'
            elif b[x][y] == '/':
                ball = 'S'
            elif b[x][y] == ' ':
                ball = ball
                
    return path

print(move_ball(['/\\/\\X', ' \\/\\W', '\\   /']))