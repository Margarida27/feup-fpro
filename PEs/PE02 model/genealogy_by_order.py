# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:06:34 2019

@author: Margarida Viera
"""

def rule(item):
    name, relation = item
    order = ('sibling', 'parent', 'cousin', 'grandparent').index(relation)
    return order, name
        
def genealogy(l):
    tree = sorted(l, key = rule, reverse = False)
    return tree

print(genealogy([('maria', 'parent'), ('matilde', 'grandparent'), ('geraldes', 'grandparent'), ('carlos', 'sibling'), ('paulo', 'sibling'), ('artur', 'grandparent'), ('pedro', 'parent'), ('alfredo', 'cousin'), ('carla', 'cousin')]))
print()
print(genealogy([('sofia', 'sibling'), ('sara', 'parent'), ('bernardo', 'parent')]))
print()
print(genealogy([('bart', 'sibling'), ('mona', 'grandparent'), ('ling', 'cousin'), ('homer', 'parent'), ('magie', 'sibling'), ('marge', 'parent'), ('abraham', 'grandparent')]))
print()
print(genealogy([('geraldes', 'cousin'), ('mario', 'parent'), ('sara', 'sibling'), ('carlos', 'cousin'), ('maria', 'parent'), ('rui', 'cousin'), ('raul', 'cousin')]))
