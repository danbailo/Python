# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:49:50 2019

@author: notebook
"""

#P048: importando um arquivo JSON
import json 

#(1)-Importa o arquivo JSON para a memória
nomeArq = 'C:/CursoPython/cinema.json'
with open(nomeArq) as f:
    filmes = json.load(f)

#(2)-Processa cada filme sequencialmente
print('----------------------------------------')
print('Tipo da variável "filmes":', type(filmes))
print('Total de filmes = ',len(filmes))

for filme in filmes:
    print('----------------------------------------')
    print('Tipo da variável "filme":', type(filme))
    print('Titulo:',filme['titulo'])
    print('Resumo:',filme['resumo'])
    print('Ano:',filme['ano'])
    print('Gênero(s):',filme['genero'])

