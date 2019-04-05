# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:16:14 2019

@author: ecorrea
"""

 #P063: Olá Vetor NumPy! 
import numpy as np  #importa a biblioteca, renomeando-a para np 
                    #(é  uma convenção... todo mundo faz isso!)

#Neste exemplo, começamos criando uma lista (lst_notas)... 
lst_notas = [7.8, 8.5, 10.0, 9.2, 5.0, 8.5, 6.4, 8.6, 7.5, 9.0]

#... e agora criamos um array a partir dessa lista (vet_notas)
vet_notas = np.array(lst_notas)

print('vet_notas = ', vet_notas)                 #imprime o vetor
print('type(vet_notas)   = ', type(vet_notas))   #imprime o tipo (ndarray) 
print('vet_notas.dtype   = ', vet_notas.dtype)   #propriedade "dtype" (float64)
print('vet_notas.ndim    = ', vet_notas.ndim)    #propriedade "ndim"  (1)
print('vet_notas.shape   = ', vet_notas.shape)   #propriedade "shape" (10)
print('vet_notas.data    = ', vet_notas.data)    #propriedade "data"
print('vet_notas.strides = ', vet_notas.strides) #propriedade "strides"

#indexação básica
print('-------------------------------------------')
print('primeiro elemento = ', vet_notas[0])
print('último elemento   = ', vet_notas[len(vet_notas)-1]) 
print('3o e 4o elementos = ',  vet_notas[2:4])  

#modifica a nota do quarto aluno
vet_notas[3] = 9.5

#imprime o novo vetor
print('-------------------------------------------')
print('vet_notas novo = ', vet_notas)
