# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 14:05:49 2019

@author: notebook
"""

#P090: JSON para DataFrame
import json 
import pandas as pd

#(1)-Importa o arquivo JSON para a memória
nomeArq = 'C:/CursoPython/cinema.json'
with open(nomeArq) as f:
    j_filmes = json.load(f)

#(2)-Transfere a informação para um DataFrame
d_filmes = pd.DataFrame(j_filmes, columns=['titulo','resumo','ano','genero'])

print(d_filmes.columns)
print('-filme 1:')
print(d_filmes.iloc[0])
print('-filme 2:')
print(d_filmes.iloc[1])
