# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:04:19 2019

@author: notebook
"""

#P027: shallow copy (referência) x deep copy (clonagem)
import copy

#1-Shallow Copy
print('* * SHALLOW COPY')
a = [1,2,3,4,5]
b = a
print('-a=',a)
print('-b=',b)

b[0] = 999
print('\t-a',a)
print('\t-b:',b)
print('\t-a is b?',a is b)     #True (o operador "is" verifica se dois objetos
                               #      têm a mesma referência)
print('\n-------------------------------------')

#2-Deep Copy utilizando a técnica de fatiamento
print('* * DEEP COPY COM FATIAMENTO')
c = [1,2,3,4,5]
d = c[:]
print('-c=',c)
print('-d=',d)
d[0] = 999
print('\t-c:',c)
print('\t-d:',d)
print('\t-c is d?',c is d)     #False
print('\n-------------------------------------')

#3-Deep Copy utilizando o módulo ‘copy’
print('* * DEEP COPY COM O MÓDULO \'copy\'')
e = copy.deepcopy(c)
print('-c=',c)
print('-e=',e)
e[0] = 999
print('\t-c:',c)
print('\t-e:',e)
print('\t-a is b?',c is d)     #False
