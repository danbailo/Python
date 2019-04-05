# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:36:17 2019

@author: ecorrea
"""


#P051 Regexps com findall()
import re

#(1)-Importa todo o arquivo para um stringão e depois o converte para uma lista
#    (cada linha do arquivo vira um elemento da lista)
nomeArq = 'C:/CursoPython/dez_filmes.txt'
f = open(nomeArq)
conteudo = f.read()
lst_filmes = conteudo.split("\n")


#(2a)-Transforma cada título de filme em um "saco de palavras" (bag of words)
print('----------------------------------------')
print('Título do filme -> saco de palavras ')

for linha in lst_filmes:
    titulo = linha.split("|")[0]
    
    lst_palavras = re.findall('([A-Za-záéíóúâêôãõçÇ]+)',titulo)
    print(lst_palavras)

