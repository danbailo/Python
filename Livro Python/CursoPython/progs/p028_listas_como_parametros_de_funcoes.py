# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:58:53 2019

@author: notebook
"""

#P028: argumentos de função: 
#      variável de tipo primitivo (int) x objeto de tipo complexo (lista)
def f_dummy(z):
    if type(z) == list: 
        z[0] = 999
    else: 
        z = 999

x = 0
lst = [1,2,3,4,5]

print('x antes de chamar a função f_dummy:',x)
f_dummy(x)
print('x depois de chamar a função f_dummy:',x)

print('----------------------------------------')

print('lst antes de chamar a função f_dummy:',lst)
f_dummy(lst)
print('lst depois de chamar a função f_dummy:',lst)
