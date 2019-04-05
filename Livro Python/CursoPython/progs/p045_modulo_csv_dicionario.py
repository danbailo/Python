# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:16:52 2019

@author: notebook
"""

 #P045: lendo um arquivo CSV como um dicionário
import csv 
with open('C:/CursoPython/paises.csv','rt') as f: 
    meu_csv = csv.DictReader(f, delimiter=';') 
    for linha in meu_csv:
       print(linha["sigla"] + ' -> populacao = ' +
             linha["populacao"])