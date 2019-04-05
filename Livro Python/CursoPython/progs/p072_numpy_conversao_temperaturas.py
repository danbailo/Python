# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:45:38 2019

@author: ecorrea
"""


#P072: Vectorization
import numpy as np  

#Conversão de Celsius para Fahrenheit sem laço  
print('-------------------------------------------')
print('* * Celsius para Fahrenheit:')
c = np.arange(-20, 101, 10,dtype=np.int16) #(-20ºC a 100ºC, de 10 em 10)
f = (c * 9 / 5 + 32)   #a fórmula é aplicada a todos os elementos do vetor
print('Celsius   =',c)      
print('Fahrenheit=',f.astype(np.int16)) #converte int16 ao exibir