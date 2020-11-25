# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:35:47 2019

@author: Margarida Viera
"""

def winning(mx):
    # full line
    for i in range(3):
        if mx[i][0] == mx[i][1] == mx[i][2]:
            return True
        
    # full column
    for j in range(3):
        if mx[0][j] == mx[1][j] == mx[2][j]:
            return True
        
    # full diagonals
    if mx[0][0] == mx[1][1] == mx[2][2]:
        return True
    
    if mx[0][2] == mx[1][1] == mx[2][0]:
        return True
    
    # not a winning move
    return False
    
    
def tic_tac_toe(board, player):
    board = board.replace(' ', '-')
    board = board.split()
    board_dict = {(0,0): 'A1',
                  (0,1): 'A2',
                  (0,2): 'A3',
                  (1,0): 'B1',
                  (1,1): 'B2',
                  (1,2): 'B3',
                  (2,0): 'C1',
                  (2,1): 'C2',
                  (2,2): 'C3',}
    
    b = board.copy()
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i] = board[i][:j] + player + board[i][j + 1:] 
                if winning(board) == True:
                    return board_dict[(i,j)]
                else:
                    board = b
    
print(tic_tac_toe(' xx\n o \noxo', 'x'))
    