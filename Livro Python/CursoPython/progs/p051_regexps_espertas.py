# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 20:45:50 2019

@author: notebook
"""

#P051 Regexps com metacaracteres no search()
import re

#(1)-Importa todo o arquivo para um stringão e depois o converte para uma lista
#    (cada linha do arquivo vira um elemento da lista)
nomeArq = 'C:/CursoPython/dez_filmes.txt'
f = open(nomeArq)
conteudo = f.read()
lst_filmes = conteudo.split("\n")

#(2a)-Encontra os filmes que começam com "O" + espaço ou "A" + espaço
print('----------------------------------------')
print('* * Filmes que começam com "O " ou "A "')

for linha in lst_filmes:
    if re.search('^O|A\s',linha):
        print(linha)

#(2b)-Encontra os filmes que possuem ano cadastrado
print('\n----------------------------------------')
print('* * Filmes com ano cadastrado')

for linha in lst_filmes:
    if re.search('\([0-9]+\)',linha):
        print(linha)

#(2c)-Encontra os filmes que possuem alguma palavra com "a" e depois "r".
#(independente do número de letras entre "a" e "r")

print('\n----------------------------------------')
print('* * Filmes com palavras que tenham "a" e depois "r"')

for linha in lst_filmes:
    if re.search('[A-Za-z]*a[A-Za-z]*r',linha):
        print(linha)


