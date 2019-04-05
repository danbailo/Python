# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:37:11 2019

@author: notebook
"""

#P039: importa arquivo inteiro para um “stringão”
nomeArq = 'C:/CursoPython/PRODUTOS.txt'
f = open(nomeArq)
conteudo = f.read()
print(conteudo)
