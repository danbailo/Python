# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:18:39 2019

@author: ecorrea
"""

#P064: Populando um vetor a partir de um arquivo texto 
import numpy as np  

vet_notas = np.genfromtxt('C:/CursoPython/NOTAS_FINAIS.txt', skip_header=1) 

print('vet_notas = ', vet_notas)                 #imprime o vetor
print('type(vet_notas)   = ', type(vet_notas))   #imprime o tipo (ndarray) 
print('vet_notas.dtype   = ', vet_notas.dtype)   #propriedade "dtype" (float64)
print('vet_notas.ndim    = ', vet_notas.ndim)    #propriedade "ndim"  (1)
print('vet_notas.shape   = ', vet_notas.shape)   #propriedade "shape" (10)
print('vet_notas.data    = ', vet_notas.data)    #propriedade "data"
print('vet_notas.strides = ', vet_notas.strides) #propriedade "strides"
