# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:49:50 2019

@author: notebook
"""

#P043: trabalhando com o módulo "csv" no modo LISTA
import csv 
with open('C:/CursoPython/paises.csv','rt') as f: 
    meu_csv = csv.reader(f, delimiter=';') 
    for linha in meu_csv:
        print(linha)
