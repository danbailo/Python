# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 13:56:41 2019

@author: notebook
"""

#P005: operadores relacionais e lógicos
print('* * * * parte 1 * * * * ')
print(4 * 2 == 8)               #True.
print(9 ** 2 == 81)             #True.
print(5 + 2 < 7)                #False.
print(5 + 2 >= 7)               #True.
print('Portela' == 'Mangueira') #False.
print(5 / 2 > 3)                #False.
print(7 % 2 != 0)               #True.


print('\n\n* * * * parte 2 * * * * ')
pais = 'Brasil'
print(pais == 'Brasil') #True.
print(pais == 'BRASIL') #False.

media_final = 7.0
if (media_final >= 7.0):
    print('com a média', media_final, 'você está aprovado')
else:
    print('reprovado')

a=10; b=100
if (a >= b):
    print('o valor de "a" é maior ou igual ao de "b"')
else:
    print('o valor de "a" é menor do que o de "b"')

print('\n\n* * * * parte 3 * * * * ')
print((4 * 2 == 8) and (9**2 >= 81))   #True.
print((1 + 1 < 3) and (9**2 > 81))     #False.
print((1 + 1 < 3) or ('flu' == 'fla')) #True.
 
