# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:27:55 2019

@author: ecorrea
"""

#P079: módulo ‘numpy.random’

#np.rand(m): produz números aleatórios uniformemente
#                distribuídos considerando a faixa de 0 a m
import numpy as np  

np.random.seed(293467)       #estabelece a semente
r1 = np.random.rand(3)       #3 núm. aleat., intervalo (0..1], dist. uniforme
r2 = np.random.randint(5,10) #um inteiro aleat., intervalo (5, 10]

print('-------------------------------------------')
print('r1 = ', r1)           #[ 0.84505198  0.59317749  0.11727527]
print('r2 = ', r2)           #8

#A biblioteca NumPy também possui geradores para diversas outras
#distribuições além da distribuição uniforme. Por exemplo:
#binomial, multinomial, Poisson, ... 

#Abaixo, um exemplo que gera números, considerando a 
#Distribuição Normal padrão (=0, =1) 
r3 = np.random.normal(size=5) 
print('-------------------------------------------')
print('r3 = ', r3) 