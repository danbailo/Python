# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:49:40 2019

@author: notebook
"""

#P087: Importação de arquivo separado por ponto e vírgula e sem cabeçalho
#(Parâmetros "sep" e "names")
import pandas as pd  

impressoras = pd.read_csv('C:/CursoPython/impressoras.txt', 
              sep=';', 
              names = ["modelo","colorida", "tipo", "preco"])

print(impressoras)    
