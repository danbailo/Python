# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:18:46 2019

@author: ecorrea
"""

 #P076: Funçoes Estatísticas aplicadas sobre um vetor 
import numpy as np  

#cria um vetor com as notas de 10 alunos
v = np.array([7.8, 8.5, 10.0, 9.2, 5.0, 8.5, 6.4, 8.6, 7.5, 9.0])

#aplica as funções estatísticas 
print('v.sum() = ', v.sum())        #soma dos valores 
print('v.max() = ', v.max())        #maior valor
print('v.min() = ', v.min())        #menor valor
print('v.mean() = ', v.mean())      #valor médio
print('np.median(v) = ', np.median(v)) #mediana (observe a sintaxe!)
print('v.std() = ', v.std())        #desvio padrão
print('v.argmax() = ', v.argmax())  #índice do maior valor
print('v.argmin() = ', v.argmin())   #índice do menor valor
