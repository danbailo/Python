# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:30:21 2019

@author: ecorrea
"""

#P066: Cria array especificando o tipo de seus elementos
import numpy as np  

a = np.array([7, 3, 5, -1, 0], dtype=np.int16) 
b = np.array([7, 3, 5, -1, 0]) 
c = np.ones(3, dtype=np.int8) 
d = np.ones(3) 

print('a = ', a, a.dtype)
print('b = ', b, b.dtype)
print('c = ', c, c.dtype)
print('d = ', d, d.dtype)

#também é possível converter explicitamente um array de um dtype para outro
#(operação conhecida como “cast”)
a = a.astype(np.float64) 
print('a = ', a, a.dtype)
