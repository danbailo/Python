# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:24:48 2019

@author: notebook
"""

#P047: FORMA CERTA de abrir arquivo na codificação utf-8
import csv 
with open('C:/CursoPython/ARTILHEIROS.csv','rt', encoding="utf-8") as f: 
    meu_csv = csv.reader(f, delimiter=',') 
    for linha in meu_csv:
       print(linha[0] + ' -> ' + linha[1])
