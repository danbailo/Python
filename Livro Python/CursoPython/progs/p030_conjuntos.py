# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:21:56 2019

@author: notebook
"""

#P030: conjuntos – criação e manipulação básica

#define quatro conjuntos
a = {0,1,2,3}
b = {2,3,4,5}
c = {1,2}

#interseção (&), união (|), diferença (-) e diferença simétrica (^) 
print (a & b)        #{2,3}
print (a | b)        #{0,1,2,3,4,5}
print (a - b)        #{0}
print (a ^ b)        #{0,1,4,5}

#está contido (<=), contém (>=)
print('----------------------------------------')
print (c <= a)        #True
print (c <= b)        #False
print (a >= c)        #True

#pertence (in), não pertence (not in)
print('----------------------------------------')
print (0 in a)        #True
print (0 in b)        #False
print (0 not in b)    #True

#incluindo (add) e removendo (remove) elementos;
print('----------------------------------------')
c.add(10)
c.add(20)
print(c)              #{1,2,10,20}
c.remove(10)
print(c)              #{1,2,20}

#esvaziando um conjunto (clear) e fazendo deep copy
print('----------------------------------------')
c.clear()           
print(c)              #set()
d = a.copy()           
print(d)              #(0,1,2,3)

#iterando sobre os elementos de um conjunto
print('----------------------------------------')
for item in b:
	print(item)
