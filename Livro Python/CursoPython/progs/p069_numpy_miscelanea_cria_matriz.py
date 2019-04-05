# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:34:09 2019

@author: ecorrea
"""

#P068: Criando matrizes de várias formas
import numpy as np  

#método básico: cria um vetor e depois aplica reshape() 
m = np.arange(10)        #cria vetor [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = m.reshape((5,2))     #transforma em uma matriz 5 x 2

#utilizando os métodos que já conhecemos: 
mz = np.zeros((4,4))               #matriz 4x4 de zeros (default=float)
mu = np.ones((3,2),dtype=np.int16) #matriz 3x2 de 1’s (forcei tipo int16)

#identity() -> cria matriz identidade 
mi = np.identity(3)                #matriz identidade 3x3

print('m = ', m)       
print('-------------------------------------------')
print('mz = ', mz)       
print('-------------------------------------------')
print('mu = ', mu)       
print('-------------------------------------------')
print('mi = ', mi)    
