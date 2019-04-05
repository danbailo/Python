# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 13:51:38 2019

@author: notebook
"""

#P088: Transformando uma coluna em índice do DataFrame
#(Parâmetro "index_col")
import pandas as pd  

impressoras = pd.read_csv('C:/CursoPython/impressoras.txt', 
              sep=';', 
              names = ["modelo","colorida", "tipo", "preco"],
              index_col = "modelo")

print(impressoras) 
print('-------------------------------------------')
print(impressoras.loc['I007']) #[0,laser,>200]
