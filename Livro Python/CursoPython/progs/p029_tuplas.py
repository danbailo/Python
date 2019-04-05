# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:12:43 2019

@author: notebook
"""

#P029: tuplas – criação e manipulação básica

#tupla com 5 elementos
t1 = (10, 20, 30, 40, 50)

#para criar uma tupla com um único elemento, 
#usa-se vírgula no final
t2 = (100,) 
  
#tupla vazia - tuple() é o método construtor de tuplas.
t3 = tuple() 

#se uma sequência é passada para tuple(ex: string ou lista),  
#a tupla é criada com os elementos da sequência
t4 = tuple('DADOS')    #('D','A','D','O',’S’)

print('t1: ', t1) 
print('tipo de dado: ', type(t1)) 
print('t1[0] -> ', t1[0])            #10 
print('t1[2:] -> ', t1[2:])          #(30,40,50) 
print('t2: ', t2) 
print('t3: ', t3) 
print('t4: ', t4) 