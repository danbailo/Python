# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:49:55 2019

@author: notebook
"""

#P014: função com parâmetro opcional
def soma_numeros(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(soma_numeros(1, 2))
print(soma_numeros(1, 2, 3))
