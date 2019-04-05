# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:08:24 2019

@author: ecorrea
"""

#P075: cópia rasa (shallow copy) x cópia profunda (deep copy)
import numpy as np  

v1 = np.arange(1,10)
c1 = v1[0:5]
print('* * * v1 e c1 -> situação inicial')
print('v1=',v1)
print('c1=',c1)

c1[0]=999
print('-------------------------------------')
print('* * * o fatiamento gera uma visão do array original (shallow copy)')
print('v1 após mudança c1[0]=',v1)
print('c1 após mudança de c1[0]=',c1)

v2 = np.arange(1,10)
c2 = v1[0:5].copy()
print('-------------------------------------')
print('* * * v2 e c2 -> situação inicial')
print('v2=',v2)
print('c2=',c2)

c2[0]=999
print('-------------------------------------')
print('* * * o fatiamento com o método copy() faz uma cópia real (deep copy)')
print('v2 após mudança c2[0]=',v2)
print('c2 após mudança de c2[0]=',c2)