# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:19:58 2019

@author: Margarida Viera
"""

import cards 
import random

def card_value(card):
    cards ={'A':11,'K':10,'Q':10,'J':10,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
    value = cards[card[1]]
    if '♠' in card or '♣' in card:
        return 2*value
    return value

# randomly play cards from each player's hand until empty
def play(seed):
    random.seed(seed)
    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)
    players = {'P1':0,'P2':0,'P3':0,'P4':0}
    move = 0
    game = []

    while hands[start_player]:
        for name in turn_order:
            move += 1
            card = cards.choose(hands[name])
            value = card_value(card)
            game.append((name,value))
            hands[name].remove(card)
            
            # when all 4 players had played (move == 4), check which one has played the valuest card
            if move == 4:
                game = sorted(game, key = lambda x: x[1])
                maximum = game[-1][1]
                
                for i in game:
                    # if that player's card has a value that matches the maximum played
                    if i[1] == maximum:
                        # then, that player receives a point
                        players[i[0]] += 1
                        
                game = []
                move = 0
    
    # list ordered by pontuaction                          
    alist = [(value,item) for value,item in players.items()]
    alist = sorted(alist,key = lambda x: x[1])
    
    # the first output will be the player known by having the maximum pontuaction
    max_points = alist[-1][1]
    output = alist[-1][0]
    
    for elem in alist:
        if elem[1] == max_points:
            
            # if another player has the same pontuaction, then he gets added to the output list
            if elem[0] not in output:
                output += ' ' + elem[0]
                
    # output is ordered by crescent order and converted to a string
    output = sorted(output.split())
    
    return ' '.join(output)

print(play(35791113))