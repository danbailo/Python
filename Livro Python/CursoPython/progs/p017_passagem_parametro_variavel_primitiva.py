# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:00:04 2019

@author: notebook
"""

#P017: passagem de parâmetro – variável de um tipo primitivo
def soma_um(numero):
    numero=numero+1
    print("somei um dentro da função: ", numero)

k=100
print('valor original de k:', k)
soma_um(k)
print('Terminou a função e k, na verdade, não mudou:', k)
