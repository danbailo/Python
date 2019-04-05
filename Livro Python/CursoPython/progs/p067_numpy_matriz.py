# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:31:32 2019

@author: ecorrea
"""

#P067: Olá Matriz NumPy! 
import numpy as np  

m = np.array([[7,8,9], [10,11,12]])    
print('m = ', m)                       #imprime a matriz
print('type(m) = ', type(m))           #imprime o tipo (ndarray) 

print('m.dtype = ',m.dtype)            #propriedade "dtype" (int32 ou int64)
print('m.ndim = ',m.ndim)              #propriedade "ndim"  (2)
print('m.shape = ',m.shape)            #propriedade "shape" (2,3)
print('m.data = ',m.data)              #propriedade "data"
print('m.strides = ',m.strides)        #propriedade "strides"

#indexação básica slicing
print('-------------------------------------------')
print('m[0,1] = ', m[0,1])         #[8]        => (1a linha, 2a coluna)
print('m[1,:] = ', m[1,:])         #[10 11 12] => (toda 2a linha)
print('m[:,2] = ', m[:,2])         #[9 12]     => (toda 3a coluna)
print('m[-1,-2:] = ', m[-1,-2:])   #[11 12]    => (última linha, 2 últ. colunas)

#modifica o valor da célula [1,2] (2a linha, 3a coluna)
m[1,2] = 999
print('-------------------------------------------')
print('m nova = ', m)              #imprime a nova matriz
