# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:22:27 2019

@author: notebook
"""

#P046: PROBLEMA ao abrir arquivo na codificação utf-8
import csv 
with open('C:/CursoPython/ARTILHEIROS.csv','rt') as f: 
    meu_csv = csv.reader(f, delimiter=',') 
    for linha in meu_csv:
       print(linha[0] + ' -> ' + linha[1])
