# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:01:08 2019

@author: ecorrea
"""

#P073: Vectorization 2
import numpy as np  

N = 5
numerador = np.ones(N)
denominador = np.arange(1,N+1)

H = sum(numerador / denominador) 

print('* * * cálculo de H = 1 + (1 / 2) + (1 / 3) + ... + (1 / N), dado N =',N)
print('* * * resposta: H = ', H)