# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 01:36:40 2019

@author: notebook
"""

#P049: gravando um arquivo JSON
import json 

#(1)-Cria a lista de dicionários
filmes = []  
filmes.append({  
    'titulo': 'Noel, Poeta da Vila',
    'resumo': 'O filme conta a história do compositor Noel Rosa',
    'ano': 2006,
    'genero': ['Biografia','Musical']
})

filmes.append({  
    'titulo': 'Edukators',
    'resumo': 'De forma criativa, dois jovens lutam contra o sistema',
    'ano': 2004,
    'genero': ['Ação','Drama','Suspense']
})

filmes.append({  
    'titulo': 'Um Conto Chinês',
    'resumo': 'Argentino mal-humorado resolve ajudar chinês desesperado',
    'ano': 2011,
    'genero': ['Comédia','Drama']
})

#(2)-Exporta os dados para um arquivo
nomeArq = 'C:/CursoPython/tres_filmes.json'

with open(nomeArq, 'w') as f_saida:  
    json.dump(filmes, f_saida,ensure_ascii=False)

print('Arquivo gravado com sucesso...')


