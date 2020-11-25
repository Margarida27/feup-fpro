# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 10:14:35 2019

@author: Margarida Viera
"""

#solution using generator
def batch_norm(alist, batch_size):
    while len(alist) > 0:
        batch = []
        l = alist.copy()
        
        if len(alist) < batch_size:
            batch_size = len(alist)
            
        for i in range(batch_size):
            batch.append(l[i])
            alist.remove(l[i])
        
        from statistics import median
        med = median(batch)
    
        for n in range(len(batch)):
            batch[n] -= med
                
        yield batch

#solution using normal function return
def batch_norm(alist, batch_size):
    batches = []
    
    while len(alist) > batch_size:
        batches.append(alist[:batch_size])
        alist = alist[batch_size:]
        
    if len(alist) != 0:
        batches.append(alist) 
    
    from statistics import median
    for batch in batches:
        med = median(batch)
        for n in range(len(batch)):
            batch[n] -= med
            
    return batches

print(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5))