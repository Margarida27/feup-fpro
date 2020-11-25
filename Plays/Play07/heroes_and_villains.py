# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:02:12 2019

@author: Margarida Viera
"""

def fight(heroes, villain):
    for heroe in heroes:
        
        if villain['health'] == 0:
            break
        
        else:
            if villain['category'] == heroe['category']: 
                
                if heroe['health'] >= villain['health']:
                    return '{0} defeated the villain and now has a score of {1}'.format(heroe['name'], heroe['score'] + 1)
                    break
                
                else:
                    villain['health'] -= round(heroe['health'] / 2, 2)
                    
    return '{0} prevailed with {1}HP left'.format(villain['name'], villain['health'])


print(fight([{'name': 'Genos', 'health': 5500, 'category': 'S', 'score': 0}, {'name': 'King', 'health': 7000, 'category': 'S', 'score': 0}, {'name': 'Blizzard of Hell', 'health': 1000, 'category': 'B', 'score': 0}, {'name': 'Saitama', 'health': 9001, 'category': 'C', 'score': 0}], {'name': 'Hero Killer', 'health': 4000, 'category': 'S'}))
print() 
print(fight([{'name': 'Superman', 'health': 6000, 'category': 'S', 'score': 3}, {'name': 'Blizzard of Hell', 'health': 2000, 'category': 'B', 'score': 7}, {'name': 'Saitama', 'health': 18002, 'category': 'C', 'score': -2}, {'name': 'Queen', 'health': 4000, 'category': 'S', 'score': 0}], {'name': 'Killer Hero', 'health': 8000, 'category': 'S'}))
                
                
                
            
            