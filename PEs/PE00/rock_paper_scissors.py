# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:25:28 2019

@author: Margarida Viera
"""

player_A = input()
player_B = input()

if player_A == 'rock' and player_B == 'scissors':
    print('The winner is A')
elif player_A == 'scissors' and player_B == 'rock':
    print('The winner is B')
elif player_A == 'scissors' and player_B == 'paper':
    print('The winner is A')
elif player_A == 'paper' and player_B == 'scissors':
    print('The winner is B')
elif player_A == 'paper' and player_B == 'rock':
    print('The winner is A')
elif player_A == 'rock' and player_B == 'paper':
    print('The winner is B')
elif player_A == 'rock' and player_B == 'rock':
    print("That's a draw")
elif player_A == 'paper' and player_B == 'paper':
    print("That's a draw")
elif player_A == 'scissors' and player_B == 'scissors':
    print("That's a draw")

    