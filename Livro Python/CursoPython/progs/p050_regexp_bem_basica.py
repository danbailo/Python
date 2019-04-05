# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 19:19:11 2019

@author: notebook
"""

#P050 Regexp basicona com search()
import re

#(1)-Importa todo o arquivo para um stringão e depois o converte para uma lista
#    (cada linha do arquivo vira um elemento da lista)
nomeArq = 'C:/CursoPython/dez_filmes.txt'
f = open(nomeArq)
conteudo = f.read()
lst_filmes = conteudo.split("\n")

#(2)-Usa search() para encontrar as linhas que possuem a palavra “Musical”
for linha in lst_filmes:
    if re.search('Musical',linha):
        print(linha)

