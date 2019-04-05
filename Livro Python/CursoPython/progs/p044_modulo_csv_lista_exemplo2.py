# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:15:00 2019

@author: notebook
"""

#P044: lê o CSV e imprime apenas 2 variáveis
import csv 
with open('C:/CursoPython/paises.csv','rt') as f: 
    meu_csv = csv.reader(f, delimiter=';') 
    i=0;
    for linha in meu_csv:
        if i > 0:         #para ignorar o cabeçalho
           print(linha[0] + ' -> população = ' + linha[4])
        i = i+1
