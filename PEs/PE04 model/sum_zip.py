# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:40:04 2019

@author: Margarida Viera
"""

# solution using normal return
def sum_zip(functions, arguments):
    output = []
    for arg in arguments:
        op = [f(arg) for f in functions]
        result = (op, sum(op))
        output.append(result)
    return output

# solution using generator
def sum_zip(functions, arguments):
    for arg in arguments:
        result = [f(arg) for f in functions]
        yield result, sum(result)

print(sum_zip([lambda x: x*2, lambda x: x**2, lambda x: -x], [-5, 10, 3]))
            
    