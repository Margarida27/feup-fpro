# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 15:12:24 2019

@author: Margarida Viera
"""

#solution using map and lambda
def invoice_totals(orders, min):
    invoice = list(map(lambda order: (order[0], order[2] * order[3]) if order[2] * order[3] > min else (order[0], (order[2] * order[3]) + 10), orders))
    return invoice

#solution using for
def invoice_totals(orders, min):
    invoice = []
    for order in orders:
        invoice.append((order[0], ((order[2] * order[3]) + 10 if order[2] * order[3] < min else order[2] * order[3]))) 
    return invoice

print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8], [77226, 'Flying Circus: Treasures, Monty Python', 3, 32.95], [88112, 'Diaries, Michael Palin', 3, 24.99]], 0))
