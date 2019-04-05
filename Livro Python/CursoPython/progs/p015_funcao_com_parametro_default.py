# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:51:21 2019

@author: notebook
"""

#P015: outra função com parâmetro com valor default 
def f_calcula(x,y,operacao='+'):
    if (operacao=='+'):
        return x+y
    elif (operacao=='-'):
        return x-y
    elif (operacao=='*'):
        return x*y
    elif (operacao=='/'):
        return x/y
    else:
        return 'operação inválida!'
    
print(f_calcula(1, 2))      #retorna 1+2 = 3
print(f_calcula(1, 2, '+')) #retorna 1+2 = 3
print(f_calcula(1, 2, '-')) #retorna 1-2 = -1
print(f_calcula(1, 2, '*')) #retorna 1*2 = 2
print(f_calcula(1, 2, '/')) #retorna 1/2 = 0.5
print(f_calcula(1, 2, '.')) #retorna 'operação inválida'
