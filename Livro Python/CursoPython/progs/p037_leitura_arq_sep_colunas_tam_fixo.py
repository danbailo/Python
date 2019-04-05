# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:25:42 2019

@author: notebook
"""

#P037: leitura de arquivo separado por colunas (tamanho fixo) 
nomeArq = 'C:/CursoPython/ARQ_COLUNAS.txt'
f = open(nomeArq)

for linha in f:
    n1 = linha[:4]
    c1 = linha[4:]
    print(n1, c1)
