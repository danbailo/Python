# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:31:53 2019

@author: notebook
"""

#P038: leitura de arquivo separado por colunas – tamanho variável
nomeArq = 'C:/CursoPython/PRODUTOS.txt'
f = open(nomeArq)

for linha in f:
    codigo = linha[:4]
    nome = linha[4:len(linha)-1]
    print(codigo, nome)