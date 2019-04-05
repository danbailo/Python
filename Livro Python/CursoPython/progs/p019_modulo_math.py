# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:35:00 2019

@author: notebook
"""

#P019: módulo ‘math’ 

import math

#constante PI
print('PI=',math.pi)     #3.141592653589793

#funções de arredondamento
x1 = 5.9
print('\n')
print(x1)
print('ceil',math.ceil(x1))
print('floor',math.floor(x1)) 
print('trunc',math.trunc(x1))  

#logaritmo 
print('\n')
x2 = 1024
print('log de ',x2, 'na base 2: ', math.log2(x2))                                 

#imprime tabela com seno, cosseno e tangente de 30, 45 e 60
#note que é preciso converter os ângulos para radianos 
print('\n')
for angulo_graus in range(30,61,15):
    angulo_radianos = math.radians(angulo_graus)
    print('\n* * * Angulo=',angulo_graus, ' graus')
    print('SENO=',round(math.sin(angulo_radianos),2))
    print('COSSENO=',round(math.cos(angulo_radianos),2))
    print('TANGENTE=',round(math.tan(angulo_radianos),2))
